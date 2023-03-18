from django.db import models

from django.contrib.auth.models import AbstractUser

from .managers import UserManager

class User(AbstractUser):

    GENRE_CHOICES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    )
    username = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Correo', blank=False, null=False)
    genre = models.CharField(max_length=1, choices = GENRE_CHOICES, verbose_name='Genero', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    class Meta:
        #db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


    def __str__(self):
        return self.first_name + ' | ' + self.email