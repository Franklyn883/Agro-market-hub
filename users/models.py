from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

#custom user
class CustomUser(AbstractUser):
    username = None
    is_deactivated = models.BooleanField(_('deactivated'), default=False)
    is_active= models.BooleanField(_("active"), default=False)
    first_name = models.CharField(_('first name'),max_length=100, null=True,blank=True)
    last_name = models.CharField(_('last name'),max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    location = models.CharField(_("location"),max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=255,null=True,blank=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    