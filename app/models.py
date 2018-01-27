from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    iban = models.CharField(max_length=250, blank=True)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)
