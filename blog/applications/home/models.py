from django.db import models
#
from model_utils.models import TimeStampedModel

# Create your models here.

class Home(TimeStampedModel):
    """Modelo para datos de la pantalla home"""
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion')
    about_title = models.CharField('Titulo Nosotros', max_length=50)
    about_text = models.TextField()
    contat_email = models.EmailField('Email Contacto', max_length=254, blank=True, null=True)
    phone = models.CharField('Telefono Contacto', max_length=20)


    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina principal'


    def __str__(self):
        return self.title



class Suscribers(TimeStampedModel):
    """Modelo para los suscriptores"""
    email = models.EmailField('Correo Electronico', max_length=254)

    class Meta:
        verbose_name = 'Suscritor'
        verbose_name_plural = 'Suscritores'


    def __str__(self):
        return self.email



class Contact(TimeStampedModel):
    """Modelo para el formulario contacto"""
    full_name = models.CharField('Nombre Completo', max_length=100)
    email = models.EmailField('Correo Electronico', max_length=254)
    messagge = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


    def __str__(self):
        return self.full_name

