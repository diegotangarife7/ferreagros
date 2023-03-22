from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=12)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.name + ' - ' + self.email
    
    class Meta:
        db_table = 'Usuarios'
        verbose_name='Usuario'
        verbose_name_plural = 'Usuarios'