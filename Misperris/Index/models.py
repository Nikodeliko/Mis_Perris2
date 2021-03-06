from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    perfil=models.CharField(max_length=20,default="Invitado")

class Region(models.Model):
	Id_Region = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=50)

class Ciudad(models.Model):
	Id_Ciudad = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=30)
	Region = models.ForeignKey(Region, null=False,blank=False, on_delete = models.CASCADE)
	
class Tipo_Vivienda(models.Model):
	Id_Tipo_Vivienda = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=30)
	
class Formulario(models.Model):
	Tipo_Vivienda = models.ForeignKey(Tipo_Vivienda, null=True,blank=False, on_delete = models.CASCADE)
	Region = models.ForeignKey(Region, null=False,blank=False, on_delete = models.CASCADE)
	Ciudad = models.ForeignKey(Ciudad, null=False,blank=False, on_delete = models.CASCADE)
	Correo = models.CharField(max_length=40)
	Run = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Fecha_Nacimineto = models.DateField()
	Fono =models.PositiveSmallIntegerField()

#class Raza_predominante(models.Model):
#	Id_Raza = models.PositiveSmallIntegerField()
#	Descripcion = models.CharField(max_length=30)

#class Tipo_estado(models.Model):
#	Id_tipo_estado = models.PositiveSmallIntegerField()
#	Descripcion = models.CharField(max_length=10)
	
#class Perros(models.Model):
#	Raza = models.ForeignKey(Raza_predominante, null=False,blank=False,on_delete = models.CASCADE)
#	Estado = models.ForeignKey(Tipo_estado,null=False,blank=False,on_delete = models.CASCADE)
#	Nombre = models.CharField(max_length=20)
#	Descripcion = models.CharField(max_length=100)
#	Foto = models.ImageField()