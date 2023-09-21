from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField( max_length=255, null=True, blank=True)
    phone_number = models.BigIntegerField( null=True, blank=True )
    address = models.CharField(max_length=255, null=True, blank=True)



