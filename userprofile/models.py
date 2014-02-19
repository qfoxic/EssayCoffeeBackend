import os
import time

from django.db import models
from django.contrib.auth.models import User

#import constants as co

def get_profile_path(instance, filename):
  return os.path.join(instance.user.username, 'profile', filename)

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  photo = models.FileField(upload_to=get_profile_path)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username

  @models.permalink
  def get_absolute_url(self):
    return  ('user_details', (), {'pk': self.pk})
  to_link = get_absolute_url

  class Meta:
    db_table = 'user_profiles'
