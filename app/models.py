from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from numbers import Number

# Create your models here.
class CustomerManager(models.Manager):
    def validation(self, **kwargs):
        print('Validation')
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        iban = kwargs['iban']
        administrator = kwargs['administrator']
        print(administrator.first_name)
        errors = {}
        if first_name == '':
            errors['name'] = 'First Name should not be empty .'

        if last_name == '':
            errors['last_name'] = 'Last Name should not be empty.'

        if iban == '' or len(iban) < 20 or (not iban.isdigit()):
            errors['iban'] = 'IBAN should not be empty and must have at least 20 numbers.'

        if errors:
            return(False, errors)
        else:
            customer = self.create(first_name=first_name, last_name=last_name, iban=iban, administrator=administrator)
            return(True, administrator.id)


class Customer(models.Model):
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    iban = models.CharField(max_length=250, blank=True)
    administrator = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = CustomerManager()


    class Meta:
        db_table = 'app_customers'
