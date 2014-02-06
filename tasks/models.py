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


class Task(models.Model):
  title = models.CharField(max_length=co.TITLE_MAX_LEN)
  ttype = models.SmallIntegerField(choices=co.TASK_TYPES,
                                   default=co.TYPE_TASK)
  access_level = models.SmallIntegerField(choices=co.ACCESS_LEVELS,
                                          default=co.PUBLIC_ACCESS)
  overview = models.TextField()
  owner = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name='owner')
  assignee = models.ForeignKey(User, null=True, blank=True,
                               related_name='assignee')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  expired = models.DateTimeField(null=True, blank=True)
  completed = models.DateTimeField(null=True, blank=True)
  end_point = models.CharField(max_length=co.MAX_STRING_LEN)
  geo_location = models.CharField(max_length=co.MAX_STRING_LEN,
                                  validators=[ValidateGeoPt], null=True)
  price = models.DecimalField(null=True, decimal_places=co.DECIMAL_PLACES,
                              max_digits=co.DECIMAL_DIGITS)
  status = models.SmallIntegerField(choices=co.TASK_STATUSES,
                                    default=co.NOT_ASSIGNED)
  category = models.ForeignKey(Categories, related_name='category')

  def __str__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return  ('task_by_id', (), {'task_id': self.id})
  to_link = get_absolute_url

  class Meta:
    db_table = 'tasks'

