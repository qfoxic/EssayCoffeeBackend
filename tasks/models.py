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

  @models.permalink
  def get_absolute_url(self):
    return  ('tasks_by_category', (), {'category_id': self.id})
  to_link = get_absolute_url

  class Meta:
    db_table = 'categories'


def get_attach_path(instance, filename):
  return os.path.join(instance.owner.username, 'attach', filename)


class Task(models.Model):
  first_name = models.CharField(max_length=co.TITLE_MAX_LEN)
  last_name = models.CharField(max_length=co.TITLE_MAX_LEN)
  gender = models.SmallIntegerField(choices=co.GENDER, blank=True,
                                    default=co.MALE)
  email = models.EmailField()
  country = models.CharField(choices=co.COUNTRIES, max_length=co.TITLE_MAX_LEN)
  phone = models.CharField(max_length=co.TITLE_MAX_LEN)
  paper_title = models.CharField(max_length=co.TITLE_MAX_LEN)
  discipline = models.CharField(choices=co.DISCIPLINES, max_length=co.TITLE_MAX_LEN)
  assigment = models.CharField(choices=co.ASSIGMENTS, max_length=co.TITLE_MAX_LEN)
  level = models.CharField(choices=co.LEVELS, max_length=co.TITLE_MAX_LEN)
  urgency = models.SmallIntegerField(choices=co.URGENCY)
  spacing = models.SmallIntegerField(choices=co.SPACING)
  page_number = models.SmallIntegerField()
  style = models.SmallIntegerField(choices=co.STYLES)
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
  #expired = models.DateTimeField()
  completed = models.DateTimeField(null=True, blank=True)
  #price = models.DecimalField(decimal_places=co.DECIMAL_PLACES,
  #                            max_digits=co.DECIMAL_DIGITS)
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

