import os
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import constants as co


def ValidateGeoPt(value):
  try:
    lat, lon = value.split(',')
    float(lat), float(lon)
  except ValueError:
    raise ValidationError('Geo Pointer should contains lat and lon decimals.')


class Categories(models.Model):
  pid = models.ForeignKey('self', blank=True, null=True)
  name = models.CharField(max_length=co.MAX_STRING_LEN)

  def __str__(self):
    return self.name

  class Meta:
    db_table = 'categories'


def get_attach_path(instance, filename):
  return os.path.join(instance.owner.username, 'attach', filename)


class Task(models.Model):
  paper_title = models.CharField(max_length=co.TITLE_MAX_LEN)
  discipline = models.CharField(choices=co.DISCIPLINES, max_length=co.TITLE_MAX_LEN, default=co.DISCIPLINES[0])
  assigment = models.CharField(choices=co.ASSIGMENTS, max_length=co.TITLE_MAX_LEN, default=co.ASSIGMENTS[0])
  level = models.CharField(choices=co.LEVELS, max_length=co.TITLE_MAX_LEN, default=co.LEVELS[0])
  urgency = models.SmallIntegerField(choices=co.URGENCY, default=co.URGENCY[0])
  spacing = models.SmallIntegerField(choices=co.SPACING, default=co.SPACING[0])
  page_number = models.SmallIntegerField()
  style = models.SmallIntegerField(choices=co.STYLES, default=co.STYLES[0])
  source_number = models.SmallIntegerField()
  instructions = models.TextField(blank=True, null=True)
  attach = models.FileField(upload_to=get_attach_path, blank=True, null=True)
  discount = models.CharField(max_length=co.TITLE_MAX_LEN, blank=True, null=True)
  accept_terms = models.BooleanField()
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
                                    default=co.NOT_ASSIGNED)
  category = models.ForeignKey(Categories, related_name='category')

  def __str__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return  ('task_view', (), {'pk': self.id})
  to_link = get_absolute_url

  class Meta:
    db_table = 'tasks'

