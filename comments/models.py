from django.db import models
from django.contrib.auth.models import User
from general.models import Task


import constants as co

class Comment(models.Model):
  title = models.CharField(max_length=co.TITLE_MAX_LEN)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  rating = models.SmallIntegerField(choices=co.COMMENT_RATINGS)
  ctask = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True,
                            related_name='ctask')
  cowner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             related_name='cowner')

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'comments'
