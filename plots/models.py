import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    key = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username


# Create your models here.
class WalmartModel(models.Model):
    """Collection walmart data"""
    upc = models.CharField(unique=True,max_length=50)
    salePrice = models.DecimalField(decimal_places=2,max_digits=12)
    name = models.CharField(max_length=10000)
    brandName = models.CharField(max_length=10000)
    modelNumber = models.CharField(max_length=10000)
    largeImage = models.CharField(max_length=10000)
    stock = models.CharField(max_length=60)
    freeShippingOver50Dollars = models.BooleanField()
    date_modified = models.DateTimeField()
