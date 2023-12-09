from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=9, unique=True)
    full_name = models.CharField(max_length=64)

    user_permissions = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

