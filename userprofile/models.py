from django.db import models
from django.contrib.auth.models import User, UserManager
from general.models import BaseModel
import constants as co


class UserProfile(BaseModel, User):
  gender = models.SmallIntegerField(choices=co.GENDER, default=co.MALE)
  country = models.CharField(choices=co.COUNTRIES, max_length=co.TITLE_MAX_LEN,
                             default=co.COUNTRIES[0])
  phone = models.CharField(max_length=co.TITLE_MAX_LEN)

  updated = models.DateTimeField(auto_now=True)
  objects = UserManager()

  def __str__(self):
    return self.username

  @models.permalink
  def get_absolute_url(self):
    return  ('user_details', (), {'pk': self.pk})
  to_link = get_absolute_url
  
  def get_group(self):
    try:
      return self.groups.values_list('name', flat=True)[0]
    except:
      return ''

  class Meta:
    db_table = 'user_profiles'
