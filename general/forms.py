from django.forms import ModelForm
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
