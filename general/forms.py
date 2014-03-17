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


class TaskSubmitForm(ModelForm):
  class Meta:
    model = Task
    fields = ['status']

  def __init__(self, request=None, *args, **kwargs):
    super(TaskSubmitForm, self).__init__(*args, **kwargs)
    self.request = request

  def clean_status(self):
    if self.instance.status == co.DRAFT:
      return co.UNPROCESSED
    raise ValidationError('Could not submit task because it is not in appropriate state.')


class TaskApproveForm(ModelForm):
  class Meta:
    model = Task
    fields = ['status']

  def __init__(self, request=None, *args, **kwargs):
    super(TaskApproveForm, self).__init__(*args, **kwargs)
    self.request = request

  def clean_status(self):
    if self.instance.status == co.UNPROCESSED:
      return co.ACTIVE
    raise ValidationError('Could not approve task because it is not in appropriate state.')


class TaskRejectForm(ModelForm):
  class Meta:
    model = Task
    fields = ['status']

  def __init__(self, request=None, *args, **kwargs):
    super(TaskRejectForm, self).__init__(*args, **kwargs)
    self.request = request

  def clean_status(self):
    if self.instance.status == co.UNPROCESSED:
      return co.REJECTED
    raise ValidationError('Could not reject task because it is not in appropriate state.')


class TaskSuspectForm(ModelForm):
  class Meta:
    model = Task
    fields = ['status']

  def __init__(self, request=None, *args, **kwargs):
    super(TaskSuspectForm, self).__init__(*args, **kwargs)
    self.request = request

  def clean_status(self):
    if self.instance.status == co.UNPROCESSED:
      return co.SUSPICIOUS
    raise ValidationError('Could not suspect task because it is not in appropriate state.')
