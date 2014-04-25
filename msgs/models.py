from django.db import models
from django.contrib.auth.models import User
from general.models import Task, BaseModel


import constants as co

class Message(BaseModel):
  title = models.CharField(max_length=co.TITLE_MAX_LEN)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  # List of user ids that opened a message in a format :ID:ID2:ID3:
  readby = models.CharField(max_length=co.MAX_STRING_LEN, blank=True)
  visibility = models.SmallIntegerField(choices=(
      (co.MSGS_ADM, 'Admin&Editor'), (co.MSGS_WRITER, 'Writer'), (co.MSGS_CUSTOMER, 'Customer')),
      default=co.MSGS_ADM)
  mtask = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True,
                            related_name='mtask')
  mowner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             related_name='mowner')

  def __str__(self):
    return self.title
  
  def get_visibility(self):
     return co.MSGS_VISIBILITY_DICT.get(self.visibility)
    
   
  class Meta:
    db_table = 'msgs'
