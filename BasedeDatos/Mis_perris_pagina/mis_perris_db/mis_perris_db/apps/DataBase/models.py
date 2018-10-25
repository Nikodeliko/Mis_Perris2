from django.db import models

# Create your models here.

class Postulante(models.Model):
    Email = models.CharField(max_length=40)
    Run = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Fecha_nacimiento = models.DateField()
    Num_telefono = models.CharField(max_length=9)


class Region (models.Model):
    Id_region = models.CharField(max_length=2)
    Descripcion = models.CharField(max_length=20)

class Ciudad (models.Model):
    Id_ciudad = models.CharField(max_length=2)
    Descripcion = models.CharField(max_length=30)

class Tipo_vivienda (models.Model):
    Id_tipo = models.CharField(max_length=2)
    Descripcion = models.CharField(max_length=25)

    
