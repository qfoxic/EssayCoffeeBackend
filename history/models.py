import os
import time
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in,user_logged_out
from general.models import Task
from userprofile.models import UserProfile
from reports.models import Report
from ftpstorage.models import Upload
from django.db.models.signals import pre_save,pre_delete
from django.dispatch import receiver


cur_user=None
def set_user(sender, request, user, **kwargs):
  global cur_user
  cur_user = user
def del_user(sender, request, user, **kwargs):
  global cur_user
  cur_user = None

user_logged_in.connect(set_user)
user_logged_out.connect(del_user)


@receiver(pre_save, sender=Task)
def save_handler(sender, **kwargs):
  global cur_user
  new_inst = kwargs['instance']
  # existing task
  if new_inst.id:
    old_inst = sender.objects.get(id=new_inst.id)
    old_values = []
    new_values = []
    fields = []
    for field in new_inst._meta.get_all_field_names():
      if field in ['ctask','ftask','rtask']:
        continue
      new_value = getattr(new_inst, field)
      old_value = getattr(old_inst, field)
      if old_value != new_value:
        fields.append(field)
        old_values.append(field + '=' + str(old_value))
        new_values.append(field + '=' + str(new_value))
    history = History(object_id=new_inst.id,
                      howner=cur_user,
                      object_type=new_inst.__class__.__name__.lower(),
                      action_type='change',
                      fields=','.join(fields),
                      old_values=','.join(old_values),
                      new_values=','.join(new_values))
    history.save()
      
  else:
    pass
    

class History(models.Model):
  howner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='howner')
  object_id = models.IntegerField()
  object_type = models.CharField(max_length=12)
  action_type = models.CharField(max_length=6,
      choices=[('add', 'add'), ('change','change'), ('delete', 'delete')])
  fields = models.CharField(max_length=500) # comma separated list of fields
  created = models.DateTimeField(auto_now_add=True)
  old_values = models.CharField(max_length=300)# field1=value:field2=value
  new_values = models.CharField(max_length=300)# the same as above

  class Meta:
    db_table = 'history'
