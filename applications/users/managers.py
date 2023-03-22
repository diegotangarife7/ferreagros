from django.db import models
from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, name, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email = email,
            name = name,
            password = password,
            is_staff = is_staff,
            is_superuser = is_superuser,
            is_active = is_active,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_user(self, email, name, password=None, **extra_fields):
        return self._create_user(email, name, password, False, False, True, **extra_fields)
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        return self._create_user(email, name, password, True, True, True, **extra_fields)