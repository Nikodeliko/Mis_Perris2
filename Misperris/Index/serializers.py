from .models import *
from rest_framework import serializers

class SerializerUsuario(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Formulario
		fields = ['Tipo_Vivienda', 'Region', 'Ciudad', 'Correo', 'Run', 'Nombre', 'Apellido', 'Fecha_Nacimiento', 'Fono']
		lookup_field = 'username'