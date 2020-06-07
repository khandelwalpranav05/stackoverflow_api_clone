from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    class Meta:
        abstract = False
