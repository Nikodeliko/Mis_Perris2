from .models import Usuario, Region, Ciudad, Tipo_Vivienda, Formulario
from rest_framework import serializers

class PerrisSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Formulario
		fields = ('Run', 'Apellido', 'Nombre', 'Correo')