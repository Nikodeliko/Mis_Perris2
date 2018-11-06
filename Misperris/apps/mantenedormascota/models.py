from django.db import models

# Create your models here.

class EstadoPerro(models.Model):
	descripcion = models.CharField(max_length=15)

	def __str__(self):
		return '{}'.format(self.descripcion)

class Perro(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=70)
    estado = models.ForeignKey(EstadoPerro, null=True, blank=True, on_delete=models.CASCADE)