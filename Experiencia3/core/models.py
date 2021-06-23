from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Cuenta(models.Model):
    Correo = models.CharField(primary_key=True,max_length=100,verbose_name='Correo')
    Nombre = models.CharField(max_length=30,verbose_name='Nombre')
    Contraseña = models.CharField(max_length=30,verbose_name='Contraseña')

    def __str__(self):
        return (self.Correo)

class Publicacion(models.Model):
    Correo = models.CharField(primary_key=True,max_length=100,verbose_name='Correo')
    Nombre = models.CharField(max_length=30,verbose_name='Nombre')
    Categoria = models.CharField(max_length=15,verbose_name='Categoria')
    Detalles = models.CharField(max_length=150,verbose_name='Detalles')
    cuenta = models.ForeignKey(Cuenta, on_delete=CASCADE)

    def __str__(self):
        return (self.Categoria)

    
