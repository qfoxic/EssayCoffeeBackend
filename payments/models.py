from django.db import models
from django.contrib.auth.models import User
from general.models import Task
import constants as co


class Payment(models.Model):
  powner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='powner')
  ptask = models.ForeignKey(Task, on_delete=models.CASCADE,
                            null=True, blank=True, related_name='ptask')
  payment_status = models.SmallIntegerField(choices=co.PAYMENT_STATUS, default=co.UNPAID)
  payment_type = models.SmallIntegerField(choices=co.PAYMENT_SYSTEMS, default=co.LIQPAY, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  values = models.CharField(max_length=5000, default='{}')# incoming data from payment system. 

  class Meta:
    db_table = 'payments'
