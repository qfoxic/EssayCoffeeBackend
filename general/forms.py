from django.forms import ModelForm, ValidationError
from general.models import Task

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
  class Meta(BaseForm.Meta):
    fields = ('site',
              'paper_title', 'discipline', 'assigment', 'level', 'urgency',
              'spacing', 'page_number', 'style', 'source_number',
              'instructions', 'attach', 'discount', 'accept_terms',
              'owner', 'assignee',
              'priority',
              'access_level',
              'revision', 'mark'
              )

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
    mail = co.ORDER_MAIL % {'first_name': self.request.user.first_name,
                            'domain': co.ADMIN_DOMAIN}
# TODO: this is a bug!!!!
#    send_mail(co.ORDER_MAIL_SUBJECT, mail, co.ADMIN_EMAIL,
#              [self.request.user.email])
    return super(TaskForm, self).save(*args, **kwargs)


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
    s = int(self.request.POST.get('status'))
    group = user.get_group()
    if (group == co.CUSTOMER_GROUP
        and not co.CheckPermissions(user, self.instance, co.CAN_SUBMIT)):
      raise ValidationError('Operation can not be performed.')
    elif group == co.ADMIN_GROUP:
      if s == co.APPROVED and not co.CheckPermissions(user, self.instance, co.CAN_APPROVE):
        raise ValidationError('Operation can not be performed.')
      elif s == co.REJECTED and not co.CheckPermissions(user, self.instance, co.CAN_REJECT):
        raise ValidationError('Operation can not be performed.')
      elif s == co.SUSPICIOUS and not co.CheckPermissions(user, self.instance, co.CAN_SUSPECT):
        raise ValidationError('Operation can not be performed.')

  def clean_status(self):
    try:
      next_status = int(self.request.POST.get('status'))
    except TypeError, ValueError:
      next_status = None
    self.check_status_allowed(next_status)
    return next_status
