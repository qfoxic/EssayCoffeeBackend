from django.forms import ModelForm, ValidationError
from general.models import Task

import constants as co

class TaskForm(ModelForm):
  def __init__(self, request=None, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    self.request = request

  class Meta:
    model = Task
    fields = [
              'paper_title', 'discipline', 'assigment', 'level', 'urgency',
              'spacing', 'page_number', 'style', 'source_number',
              'instructions', 'attach', 'discount', 'accept_terms',
              'owner']

  def clean_owner(self):
    """Specifies default User parameter."""
    return self.request.user

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

  def clean_status(self):
    try:
      next_status = int(self.request.POST.get('status'))
    except TypeError, ValueError:
      next_status = None 
    self.check_status_allowed(next_status)
    return next_status

