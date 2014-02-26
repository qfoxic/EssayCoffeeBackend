import os

from django.db import models
from django.contrib.auth.models import User, UserManager

import constants as co


class UserProfile(User):
  gender = models.SmallIntegerField(choices=co.GENDER, blank=True,
                                    default=co.MALE)
  country = models.CharField(choices=co.COUNTRIES, max_length=co.TITLE_MAX_LEN)
  phone = models.CharField(max_length=co.TITLE_MAX_LEN)

  updated = models.DateTimeField(auto_now=True)
  objects = UserManager()

  def __str__(self):
    return self.username

  @models.permalink
  def get_absolute_url(self):
    return  ('user_details', (), {'pk': self.pk})
  to_link = get_absolute_url

  class Meta:
    db_table = 'user_profiles'
