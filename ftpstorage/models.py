import os
import time
from django.db import models
from django.contrib.auth.models import User
from general.models import Task
from django.core.exceptions import ValidationError

import constants as co

  
def get_attach_path(instance, filename):
  #return os.path.join(instance.fowner.username, filename)
  return instance.fowner.username + '/' + filename


class Upload(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  attach = models.FileField(upload_to=get_attach_path, blank=True, null=True)
  fowner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                            related_name='fowner')
  ftask = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True,
                            related_name='ftask')
  access_level = models.CharField(choices=co.ACCESS_LEVELS,
                                  default=co.PRIVATE_ACCESS,
                                  max_length=1)

  class Meta:
    db_table = 'uploads'

  def delete(self, using=None):
    self.attach.delete()
    super(Upload, self).delete(using)