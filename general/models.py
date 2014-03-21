import os
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
  instructions = models.TextField(max_length=co.INSTRUCTION_MAX_LEN,
                                  validators=[ValidateMinSize(100)])
  attach = models.FileField(upload_to=get_attach_path, blank=True, null=True)
  discount = models.CharField(max_length=co.TITLE_MAX_LEN)
  accept_terms = models.BooleanField(validators=[ValidateTerms])
  #######################################
  ttype = models.SmallIntegerField(choices=co.TASK_TYPES, blank=True,
                                   default=co.TYPE_TASK)
  access_level = models.SmallIntegerField(choices=co.ACCESS_LEVELS, blank=True,
                                          default=co.PUBLIC_ACCESS)
  owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                            related_name='owner')
  assignee = models.ForeignKey(User, null=True, blank=True,
                               related_name='assignee')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  completed = models.DateTimeField(null=True, blank=True)
  status = models.SmallIntegerField(choices=co.TASK_STATUSES, blank=True,
                                    default=co.DRAFT)

  def __str__(self):
    return self.paper_title

  get_status = lambda self: co.TASK_STATUSES_DICT.get(self.status)
  get_discipline = lambda self: co.DISCIPLINES_DICT.get(self.discipline)
  get_spacing = lambda self: co.SPACING_DICT.get(self.spacing)
  get_assigment = lambda self: co.ASSIGMENTS_DICT.get(self.assigment)
  get_level = lambda self: co.LEVELS_DICT.get(self.level)
  get_urgency = lambda self: co.URGENCY_DICT.get(self.urgency)  
  get_style = lambda self: co.STYLES_DICT.get(self.style) 

  @models.permalink
  def get_absolute_url(self):
    return  ('task_view', (), {'pk': self.id})
  to_link = get_absolute_url


  class Meta:
    db_table = 'tasks'

