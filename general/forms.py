from django.forms import ModelForm, ValidationError
from general.models import Task

import constants as co

class TaskForm(ModelForm):
  def __init__(self, request=None, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    self.request = request

  class Meta:
    model = Task
    fields = ['site',
              'paper_title', 'discipline', 'assigment', 'level', 'urgency',
              'spacing', 'page_number', 'style', 'source_number',
              'instructions', 'attach', 'discount', 'accept_terms',
              'owner',
              'priority', 'access_level', 'in_review', 'mark']

  def clean_owner(self):
    """Specifies default User parameter."""
    if self.initial.get('owner'):
      return self.initial.get('owner')
    return self.request.user

  def clean_site(self):
    """Specifies default Host parameter."""
    if self.initial.get('site'):
      return self.initial.get('site')
    return self.request.get_host()

  def check_permissions(self, cleaned_data):
    """Raise an exception if user can't perform a status change."""
    user = self.request.user
    if not co.CheckPermissions(user, self.instance, co.CAN_EDIT):
      raise ValidationError('Operation can not be performed.')

  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(TaskForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data

  def save(self, *args, **kwargs):
    # send email
    mail = co.ORDER_MAIL % {'first_name': self.request.user.first_name,
                            'domain': co.ADMIN_DOMAIN}
# TODO: this is a bug!!!!
#    send_mail(co.ORDER_MAIL_SUBJECT, mail, co.ADMIN_EMAIL,
#              [self.request.user.email])
    return super(TaskForm, self).save(*args, **kwargs)


class SwitchStatusForm(ModelForm):
  class Meta:
    model = Task
    fields = ['status']

  def __init__(self, request=None, *args, **kwargs):
    super(SwitchStatusForm, self).__init__(*args, **kwargs)
    self.request = request

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
    group = user.get_group()
    if (group == co.CUSTOMER_GROUP
        and not co.CheckPermissions(user, self.instance, co.CAN_SUBMIT)):
      raise ValidationError('Operation can not be performed.')
    elif (group == co.ADMIN_GROUP
          and not co.CheckPermissions(user, self.instance, co.CAN_DO_ADMIN_ACTIONS)):
      raise ValidationError('Operation can not be performed.')

  def clean_status(self):
    try:
      next_status = int(self.request.POST.get('status'))
    except TypeError, ValueError:
      next_status = None
    self.check_status_allowed(next_status)
    return next_status

  def clean(self):
    # Check some conditions before saving a form.
    cleaned_data = super(SwitchStatusForm, self).clean()
    self.check_permissions(cleaned_data)
    return cleaned_data
