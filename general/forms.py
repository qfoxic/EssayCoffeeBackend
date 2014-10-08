from django.forms import ModelForm, ValidationError, FileField
from general.models import Task
from ftpstorage.models import Upload
from userprofile.models import UserProfile
from django.core.mail import send_mail

import constants as co

class BaseForm(ModelForm):
  class Meta:
    model = Task
    fields = () 

  def __init__(self, request=None, *args, **kwargs):
    super(BaseForm, self).__init__(*args, **kwargs)
    self.request = request

  def clean(self, *args, **kwargs):
    cleaned_data = super(BaseForm, self).clean()
    self.check_permissions(cleaned_data)
    return super(BaseForm, self).clean(*args, **kwargs)


class TaskForm(BaseForm):
  attach = FileField(required=False)
  class Meta(BaseForm.Meta):
    fields = ('site',
              'paper_title', 'discipline', 'assigment', 'level', 'urgency',
              'spacing', 'page_number', 'style', 'source_number',
              'instructions', 'discount', 'accept_terms',
              'owner', 'assignee',
              'priority', 'attach',
              'access_level',
              'revision', 'mark'
              )

  def __init__(self, request=None, *args, **kwargs):
    super(TaskForm, self).__init__(request, *args, **kwargs)
    self.writers = UserProfile.objects.filter(groups__name=co.WRITER_GROUP)
    self.fields['assignee'].queryset = self.writers

  def clean_owner(self):
    """Specifies default User parameter."""
    return self.request.user

  def clean_site(self):
    """Specifies default Host parameter."""
    return self.request.get_host()
  
  def check_permissions(self, cleaned_data):
    """Raise an exception if user can't perform a status change."""
    user = self.request.user
    if not co.CheckPermissions(user, self.instance, co.CAN_EDIT):
      raise ValidationError('Operation can not be performed.')

  def save(self, *args, **kwargs):
    # send email
    #mail = co.ORDER_MAIL % {'first_name': self.request.user.first_name,
    #                        'domain': co.ADMIN_DOMAIN}
    # TODO: this is a bug!!!!
    #    send_mail(co.ORDER_MAIL_SUBJECT, mail, co.ADMIN_EMAIL,
    #              [self.request.user.email])
    is_new = True
    if self.instance.pk:
      is_new = False

    res = super(TaskForm, self).save(*args, **kwargs)
    if is_new:
      if self.cleaned_data['attach']:
        upload = Upload(attach=self.cleaned_data['attach'],
                        ftask=self.instance, fowner=self.request.user,
                        access_level=co.PRIVATE_ACCESS)
        upload.save()
    return res


class LockTaskForm(BaseForm):
  def check_permissions(self, cleaned_data):
    """Raise an exception if user can't perform a status change."""
    user = self.request.user
    can_lock = co.CheckPermissions(user, self.instance, co.CAN_LOCK)
    is_locked = self.instance.is_locked(user)
    if not can_lock:
      raise ValidationError('Operation can not be performed.')
    if is_locked:
      raise ValidationError('Task is already locked.')
    self.instance.lock(self.request.user)


class UnlockTaskForm(BaseForm):
  def check_permissions(self, cleaned_data):
    """Raise an exception if user can't perform a status change."""
    user = self.request.user
    can_unlock = co.CheckPermissions(user, self.instance, co.CAN_UNLOCK)
    is_locked = self.instance.is_locked(user, by_user=True)
    if not can_unlock:
      raise ValidationError('Operation can not be performed.')
    if is_locked:
      self.instance.unlock(self.request.user)
    else:
      raise ValidationError('User can\'t unclock a task.')


class SwitchStatusForm(BaseForm):
  class Meta(BaseForm.Meta):
    fields = ('status',)

  def check_status_allowed(self, next_status):
    """Raise an exception if status isn't allowed.
    Args:
      next_status: status to set.
    """
    switch_table = co.STATUS_SWITCH_TABLE
    cur_status = self.instance.status
    allowed = switch_table.get(cur_status)
    if not allowed:
      raise ValidationError('That status can not be modified.')
    if not next_status in allowed:
      raise ValidationError('This status is inappropriate. You can not set to it.')

  def check_permissions(self, cleaned_data):
    """Raise an exception if user can't perform a status change."""
    user = self.request.user
    status = int(self.request.POST.get('status'))
    group = user.get_group()
    if (group == co.CUSTOMER_GROUP
        and not co.CheckPermissions(user, self.instance, co.CAN_SUBMIT)):
      raise ValidationError('Operation can not be performed.')
    elif group == co.ADMIN_GROUP:
      if status == co.PROCESSING and not co.CheckPermissions(user, self.instance, co.CAN_APPROVE):
        raise ValidationError('Operation can not be performed.')
      elif status == co.REJECTED and not co.CheckPermissions(user, self.instance, co.CAN_REJECT):
        raise ValidationError('Operation can not be performed.')
      elif status == co.SUSPICIOUS and not co.CheckPermissions(user, self.instance, co.CAN_SUSPECT):
        raise ValidationError('Operation can not be performed.')
    elif group == co.WRITER_GROUP:
      if status == co.SENT and not co.CheckPermissions(user, self.instance, co.CAN_SEND):
        raise ValidationError('Operation can not be performed.')
      if status == co.SENT and not self.instance.is_locked(user, by_user=True):
        raise ValidationError('Please lock a task before make it SENT.')
        

  def clean_status(self):
    try:
      next_status = int(self.request.POST.get('status'))
    except (TypeError, ValueError):
      next_status = None
    self.check_status_allowed(next_status)
    return next_status
  
  def save(self, *args, **kwargs):
    # When go by path UNPROCESSED->PROCESSING.
    # make task publicly visible.
    # Status that we are going to switch to.
    status = self.cleaned_data['status']
    if status == co.PROCESSING:
      self.instance.access_level = co.PUBLIC_ACCESS
    elif status == co.COMPLETED:
      user = self.request.user 
      try:
        send_mail('Order has been completed.',
                  co.ORDER_FINISHED_EMAIL % {
                       'first_name': user.first_name,
                       'order_title': self.instance.paper_title,
                       'order_id': self.instance.pk},
                  co.ADMIN_EMAIL,
                  [user.email])
      except:
        pass 
    return super(SwitchStatusForm, self).save(*args, **kwargs)

class ForceSwitchStatusForm(BaseForm):
  class Meta(BaseForm.Meta):
    fields = ('status',)
  
  def clean_status(self):
    try:
      status = int(self.request.POST.get('status'))
      # Very simple verification.
      co.TASK_STATUSES_DICT[status]
    except (TypeError, ValueError, KeyError):
      raise ValidationError('Status does not exists.') 
    return status
  
  def check_permissions(self, cleaned_data):
    pass
