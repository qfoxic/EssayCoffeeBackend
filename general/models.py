import os, re
import time
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from history.models import new_event, change_event, delete_event

import constants as co

  

def ValidateTerms(value):
  if not value:
    raise ValidationError('Please accept terms.')


def ValidateEmptySelect(value):
  if not value:
    raise ValidationError('Please select an option.')


def ValidateMinSize(size):
  def Validate(value):
    if len(value) < size:
      raise ValidationError('Size should be at least %s' % size)
  return Validate

def get_pid(path):
  mo = re.match(r'^/\w+/(\d+)/.*', path)
  if mo and mo.groups(): 
    return mo.group(1)
  else:
    return None 
    
# Main purpose of that class is to create events on each action.
class BaseModel(models.Model):
  class Meta:
    abstract = True
  
  def save(self, *args, **kwargs):
    # instance is new.
    if not self.id:
      # Save an item before event.
      super(BaseModel, self).save(*args, **kwargs)
      if hasattr(self.__class__, 'cur_rqst'):
        #import pdb; pdb.set_trace()
        new_event(self.__class__.cur_rqst.user, self, get_pid(self.__class__.cur_rqst.path))
    else:
      if hasattr(self.__class__, 'cur_rqst'):
        change_event(self.__class__.cur_rqst.user, self, get_pid(self.__class__.cur_rqst.path))
      super(BaseModel, self).save(*args, **kwargs)
  
  def delete(self, *args, **kwargs):
    if hasattr(self.__class__, 'cur_rqst'):
      delete_event(self.__class__.cur_rqst.user, self, get_pid(self.__class__.cur_rqst.path))
    super(BaseModel, self).delete(*args, **kwargs)


class Task(BaseModel):
  paper_title = models.CharField(max_length=co.TITLE_MAX_LEN, validators=[ValidateMinSize(4)])
  discipline = models.CharField(choices=co.DISCIPLINES, max_length=co.TITLE_MAX_LEN,
                                default=co.DISCIPLINES[0], validators=[ValidateEmptySelect])
  assigment = models.CharField(choices=co.ASSIGMENTS, max_length=co.TITLE_MAX_LEN,
                               default=co.ASSIGMENTS[0], validators=[ValidateEmptySelect])
  level = models.CharField(choices=co.LEVELS, max_length=co.TITLE_MAX_LEN, default=co.LEVELS[0])
  urgency = models.IntegerField(choices=co.URGENCY, default=co.URGENCY[0],
                               validators=[ValidateEmptySelect])
  spacing = models.SmallIntegerField(choices=co.SPACING, default=co.SPACING[0],
                                     validators=[ValidateEmptySelect])
  page_number = models.SmallIntegerField()
  style = models.SmallIntegerField(choices=co.STYLES, default=co.STYLES[0],
                                   validators=[ValidateEmptySelect])
  source_number = models.SmallIntegerField()
  mark = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
  instructions = models.TextField(max_length=co.INSTRUCTION_MAX_LEN,
                                  validators=[ValidateMinSize(100)])
  discount = models.CharField(max_length=co.TITLE_MAX_LEN, null=True, blank=True)
  accept_terms = models.BooleanField(validators=[ValidateTerms])
  payment_status = models.SmallIntegerField(choices=co.PAYMENT_STATUS, default=co.UNPAID)
  priority = models.BooleanField(default=False, blank=True)
  #######################################
  site = models.TextField(blank=True,null=True)
  ttype = models.SmallIntegerField(choices=co.TASK_TYPES, blank=True,
                                   default=co.TYPE_TASK)
  access_level = models.CharField(choices=co.ACCESS_LEVELS,
                                  default=co.PRIVATE_ACCESS,
                                  max_length=1)
  revision = models.BooleanField(default=False, blank=True)
  # Users
  owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                            related_name='owner')
  assignee = models.ForeignKey(User, null=True, blank=True,
                               related_name='assignee')
  manager = models.ForeignKey(User, null=True, blank=True,
                              related_name='manager')
  editor = models.ForeignKey(User, null=True, blank=True,
                             related_name='editor')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  completed = models.DateTimeField(null=True, blank=True)
  status = models.SmallIntegerField(choices=co.TASK_STATUSES, blank=True,
                                    default=co.DRAFT)

  def __str__(self):
    return self.paper_title

  get_status = lambda self: co.TASK_STATUSES_DICT.get(self.status)
  get_payment_status = lambda self: co.PAYMENT_STATUS_DICT.get(self.payment_status)
  get_discipline = lambda self: co.DISCIPLINES_DICT.get(self.discipline)
  get_spacing = lambda self: co.SPACING_DICT.get(self.spacing)
  get_assigment = lambda self: co.ASSIGMENTS_DICT.get(self.assigment)
  get_level = lambda self: co.LEVELS_DICT.get(self.level)
  get_urgency = lambda self: co.URGENCY_DICT.get(self.urgency)  
  get_style = lambda self: co.STYLES_DICT.get(self.style)
  get_access_level = lambda self: co.ACCESS_LEVELS_DICT.get(self.access_level)
  
  def admin_deadline(self):
    deadline = time.mktime(self.created.timetuple())+self.urgency
    return deadline

  def writer_deadline(self):
    deadline = time.mktime(self.created.timetuple())+(
        self.urgency * co.WRITER_DEADLINE_PERCENT)
    return deadline
  
  def is_locked(self, user, by_user=False):
    """If by_user is specified then check whether it is locked by that user."""
    group = user.get_group()
    if group == co.WRITER_GROUP:
      return self.assignee == user if by_user else self.assignee is not None
    elif group == co.ADMIN_GROUP:
      return self.manager == user if by_user else self.manager is not None
    elif group == co.EDITOR_GROUP:
      return self.editor == user if by_user else self.editor is not None
    return False
  
  def lock(self, user):
    group = user.get_group()
    if group == co.WRITER_GROUP:
      self.assignee = user 
    elif group == co.ADMIN_GROUP:
      self.manager = user
    elif group == co.EDITOR_GROUP:
      self.editor = user
   
  def unlock(self, user):
    group = user.get_group()
    if group == co.ADMIN_GROUP:
      self.manager = None 
    elif group == co.EDITOR_GROUP:
      self.editor = None
  
  def get_price(self):
    percents = co.ITEMS_PERCENTS
    mpp = co.MAX_PAGE_PRICE
    assig_percent = percents['assigments'].get(self.assigment, 0)
    level_percent = percents['levels'].get(self.level, 0)
    urgency_percent = percents['urgency'].get(self.urgency, 0)
    spacing_percent = percents['spacing'].get(self.spacing, 0)
    page_sum = (mpp*assig_percent + mpp*level_percent + mpp*urgency_percent)
    return (page_sum + page_sum*spacing_percent) * self.page_number
 
  @classmethod 
  def get_finished_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.COMPLETED).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.COMPLETED).filter(**kwargs)

  @classmethod 
  def get_all_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(**kwargs).count()
    return cls.objects.filter(**kwargs)

  @classmethod 
  def get_draft_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.DRAFT).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.DRAFT).filter(**kwargs)

  @classmethod 
  def get_sent_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.SENT).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.SENT).filter(**kwargs)

  @classmethod 
  def get_all_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(**kwargs).count()
    return cls.objects.filter(**kwargs)
  
  @classmethod 
  def get_unprocessed_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.UNPROCESSED).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.UNPROCESSED).filter(**kwargs)

  @classmethod 
  def get_suspicious_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.SUSPICIOUS).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.SUSPICIOUS).filter(**kwargs)

  @classmethod 
  def get_processing_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.PROCESSING).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.PROCESSING).filter(**kwargs)

  @classmethod 
  def get_rejected_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.REJECTED).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.REJECTED).filter(**kwargs)

  @classmethod 
  def get_expired_tasks(cls, count_only, **kwargs):
    where = ['urgency-TIMESTAMPDIFF(SECOND, created, now()) <= 0']
    expired_tasks = Task.objects.extra(where=where).filter(**kwargs)
    if count_only:
      return expired_tasks.count()
    return expired_tasks
  
  @models.permalink
  def get_absolute_url(self):
    return  ('task_view', (), {'pk': self.id})
  to_link = get_absolute_url

  class Meta:
    db_table = 'tasks'
  
  def save(self, *args, **kwargs):
    flds = set(self._meta.get_all_field_names())
    if self.pk or self.id:
      # Don't update fields below.
      flds = flds.difference(['owner', 'site', 'id', 'mtask', 'rtask', 'ftask', 'howner', 'ctask'])
      kwargs.update({'update_fields': flds})
      return super(Task, self).save(*args, **kwargs)
    return super(Task, self).save(*args, **kwargs)

