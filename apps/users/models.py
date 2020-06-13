from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import xUserManager


class Xusers(AbstractBaseUser):
    
    email = models.EmailField( max_length=254, unique=True)
    users_fullname = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=90)
    users_created = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = xUserManager()
    
    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'apps_users0'
        managed = True
        
    


# Create your models here.
