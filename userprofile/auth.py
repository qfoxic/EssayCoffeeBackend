from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from userprofile.getuser import get_current_request

import constants as co

class UserProfileBackend(ModelBackend):
  def authenticate(self, username=None, password=None):
    try:
      user = self.user_class.objects.get(username=username)
      request_host = get_current_request().get_host()
      if not user.is_superuser and settings.ACTIVE_GROUP != user.get_group():
        return None
      # Check site this request is coming from. Only for customers.
      if user.get_group() == co.CUSTOMER_GROUP and user.site != request_host:
        return None
      if user.check_password(password):
        return user
    except self.user_class.DoesNotExist:
      return None

  def get_user(self, user_id):
    try:
      return self.user_class.objects.get(pk=user_id)
    except self.user_class.DoesNotExist:
      return None

  @property
  def user_class(self):
    if not hasattr(self, '_user_class'):
      self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
      if not self._user_class:
        raise ImproperlyConfigured('Could not get custom user model')
    return self._user_class
