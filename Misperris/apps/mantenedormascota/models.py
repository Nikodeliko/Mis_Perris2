from django.db import models

# Create your models here.

class EstadoPerro(models.Model):
	descripcion = models.CharField(max_length=15)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Perro(models.Model):
	fotografia = models.ImageField(upload_to='profile_pics/%Y-%m-%d/')
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=70)
	estado = models.ForeignKey(EstadoPerro, on_delete=models.CASCADE)
