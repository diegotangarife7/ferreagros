from django.db import models

from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager

class User(AbstractUser):
    pass