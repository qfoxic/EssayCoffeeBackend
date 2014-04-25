import os
import time
from django.db import models
from django.contrib.auth.models import User

CHANGE_EVENT = 'change'
NEW_EVENT = 'new'
DELETE_EVENT = 'delete'
ELIMINATION_FIELDS = ['mtask','ftask','rtask', 'logentry', 'manager',
    'howner', 'groups', 'fowner', 'editor', 'assignee',
    'ctask', 'owner', 'site', 'user_permissions', 'rowner', 'mowner', ]


def _add_event(user, action, obj, fields, old_values, new_values, pid = None):
  """user - current user.
     obj - model instance.
     fields - list of changed fields.
     old_values - list of old values ['value=param', 'value1=param'].
     new_values - list of new values ['value=param', 'value1=param'].
  """
  if not user.is_authenticated():
    user = None
    
  history = History(object_id=obj.id,
                    howner=user,
                    parent_id=pid,
                    object_type=obj.__class__.__name__,
                    action_type=action,
                    fields=','.join(fields),
                    old_values=','.join(old_values),
                    new_values=','.join(new_values))
  history.save()
  return history


def _obj_diff(old_inst, new_inst):
  """Returns difference between two objects."""
  old_values = []
  new_values = []
  fields = []
  for field in new_inst._meta.get_all_field_names():
    if field in ELIMINATION_FIELDS:
      continue
    try:
      new_value = getattr(new_inst, field)
      old_value = getattr(old_inst, field)
    except AttributeError:
      continue
    if old_value != new_value:
      fields.append(field)
      old_values.append(field + '=' + str(old_value))
      new_values.append(field + '=' + str(new_value))
  return fields, old_values, new_values


def new_event(user, inst, pid = None):
  """inst - old instance."""
  # Don't create an event if instance isn't new.
  if not inst.id:
    return
  # No need to display difference between objects if it is new.
  fields, old_values, new_values = _obj_diff(inst, inst)
  return _add_event(user, NEW_EVENT, inst, fields, old_values, new_values, pid)


def change_event(user, inst, pid = None):
  """Have to be called before an inst is going to be saved.
     user - current user.
     inst - model instance before saving.
  """
  # Don't create an event if instance is new.
  if not inst.id:
    return
  old_inst = inst.__class__.objects.get(id=inst.id)
  fields, old_values, new_values = _obj_diff(old_inst, inst)
  return _add_event(user, CHANGE_EVENT, inst, fields, old_values, new_values, pid)


def delete_event(user, inst, pid = None):
  # Don't create an event if instance is new.
  if not inst.id:
    return
  # No need to display difference between objects if it is new.
  fields, old_values, new_values = _obj_diff(inst, inst)
  return _add_event(user, DELETE_EVENT, inst, fields, old_values, new_values, pid)


def list_task_events(task_id):
  sql = ('SELECT id,howner_id,object_id,object_type,action_type,history.created,old_values,new_values'
         ' FROM history WHERE object_type IN ("Upload", "Message", "Task", "Report") AND parent_id=%(pid)s')
  return History.objects.raw(sql%{'pid':task_id})


class History(models.Model):
  howner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='howner')
  parent_id = models.IntegerField( null=True, blank=True )
  object_id = models.IntegerField()
  object_type = models.CharField(max_length=12)
  action_type = models.CharField(max_length=6,
      choices=[(NEW_EVENT, 'new'), (CHANGE_EVENT,'change'), (DELETE_EVENT, 'delete')])
  fields = models.CharField(max_length=1000) # comma separated list of fields
  created = models.DateTimeField(auto_now_add=True)
  old_values = models.CharField(max_length=1500)# field1=value,field2=value
  new_values = models.CharField(max_length=1500)# the same as above

  class Meta:
    db_table = 'history'
