import os
import datetime
import time
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

def get_attach_path(instance, filename):
  return os.path.join(instance.owner.username, 'attach', filename)


class Task(models.Model):
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
  attach = models.FileField(upload_to=get_attach_path, blank=True, null=True)
  discount = models.CharField(max_length=co.TITLE_MAX_LEN)
  accept_terms = models.BooleanField(validators=[ValidateTerms])
  payment_status = models.SmallIntegerField(choices=co.PAYMENT_STATUS, default=co.UNPAID)
  priority = models.SmallIntegerField(choices=co.TASK_PRIORITY, default=co.LOW,
                                      validators=[ValidateEmptySelect])
  #######################################
  site = models.TextField(blank=True,null=True)
  ttype = models.SmallIntegerField(choices=co.TASK_TYPES, blank=True,
                                   default=co.TYPE_TASK)
  access_level = models.SmallIntegerField(choices=co.ACCESS_LEVELS,
                                          default=co.PUBLIC_ACCESS)
  in_review = models.BooleanField(default=False)
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
  get_priority = lambda self: co.TASK_PRIORITY_DICT.get(self.priority)
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
    deadline = time.mktime(self.created.timetuple())+self.urgency
    return deadline * co.WRITER_DEADLINE_PERCENT

  @classmethod 
  def get_finished_tasks(cls, count_only, **kwargs):
    if count_only:
      return cls.objects.filter(status__exact=co.COMPLETED).filter(**kwargs).count()
    return cls.objects.filter(status__exact=co.COMPLETED).filter(**kwargs)
  
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

