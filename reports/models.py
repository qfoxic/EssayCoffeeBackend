from django.db import models
from django.contrib.auth.models import User
from general.models import Task, BaseModel


import constants as co

class Report(BaseModel):
  title = models.CharField(max_length=co.TITLE_MAX_LEN)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  rtask = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True,
                            related_name='rtask')
  rowner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             related_name='rowner')

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'reports'
