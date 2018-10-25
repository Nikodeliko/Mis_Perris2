from django.db import models

# Create your models here.
class Region(models.Model):
	Id_Region = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=50)

class Ciudad(models.Model):
	Region = models.ForeignKey(Region, null=False,blank=False, on_delete = models.CASCADE)
	Id_Ciudad = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=30)
	
class Tipo_Vivienda(models.Model):
	Id_Tipo_Vivienda = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=30)
	
class Usuario(models.Model):
	Tipo_Vivienda = models.ForeignKey(Tipo_Vivienda, null=False,blank=False, on_delete = models.CASCADE)
	Correo = models.CharField(max_length=40)
	Run = models.CharField(max_length=10)
	Nombre = models.CharField(max_length=100)
	Apellido = models.CharField(max_length=100)
	Fecha_Nacimineto = models.DateField()
	Fono =models.PositiveSmallIntegerField()
	Region = models.ForeignKey(Region, null=False,blank=False, on_delete = models.CASCADE)
	Ciudad = models.ForeignKey(Ciudad, null=False,blank=False, on_delete = models.CASCADE)

	
class Raza_predominante(models.Model):
	Id_Raza = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=30)

class Tipo_estado(models.Model):
	Id_tipo_estado = models.PositiveSmallIntegerField()
	Descripcion = models.CharField(max_length=10)
	
class Perros(models.Model):
	Raza = models.ForeignKey(Raza_predominante, null=False,blank=False,on_delete = models.CASCADE)
	Estado = models.ForeignKey(Tipo_estado,null=False,blank=False,on_delete = models.CASCADE)
	Nombre = models.CharField(max_length=20)
	Descripcion = models.CharField(max_length=100)
	Foto = models.ImageField()
	

		

	
	



	
