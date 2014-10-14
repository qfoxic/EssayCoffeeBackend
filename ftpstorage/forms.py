from django.forms import ValidationError
from ftpstorage.models import Upload
from general.models import Task
from general.forms import BaseForm
from django.contrib import messages


import constants as co


class UploadForm(BaseForm):
  class Meta(BaseForm.Meta):
    model = Upload
    fields = ('attach', 'fowner', 'access_level', 'ftask')

  def __init__(self, request=None, task_id=None, *args, **kwargs):
    super(UploadForm, self).__init__(*args, **kwargs)
    self.request = request
    self.task_id = task_id
  
  def clean_fowner(self):
    """Specifies default User parameter."""
    return self.request.user

  def clean_ftask(self):
    """Specifies default task for a comment."""
    return Task.objects.get(pk=self.task_id)
  
  def check_permissions(self, cleaned_data):
    """Raises an exception if there are no permissions to save a form."""
    if not co.CheckPermissions(self.request.user,
        self.cleaned_data['ftask'], co.CAN_UPLOAD, 'upload'):
      raise ValidationError('You can not upload file.')

  def save(self):
    filename = self.instance.get_filename()
    length = len(self.instance.attach) / 1024 / 1024
    try:
      if length > 5:
        raise Exception('A file size should not exceeds 5MB.')
    except Exception, e:
      messages.error(self.request, str(e))
      return
    messages.success(self.request, 'File was successfully uploaded.')
    return super(UploadForm, self).save()


