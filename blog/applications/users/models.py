from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = '2'

    CHOICES_GENDER = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro')
    )

    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=150)
    ocupation = models.CharField('Ocupacion', max_length=50, blank=True)
    genero = models.CharField('Genero', max_length=50, choices=CHOICES_GENDER, blank=True)
    date_birth = models.DateField('Fecha Nacimiento', blank=True, null=True)    
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']


    def get_full_name(self):
        return self.full_name
    

    def get_email(self):
        return self.email
