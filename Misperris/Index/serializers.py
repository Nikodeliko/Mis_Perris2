from .models import *
from rest_framework import serializers

class SerializerUsuario(serializers.HyperLinkedModelSerielizer):
	class Meta:
		model = Formulario
		fields = ('Run','Nombre', 'Apellido', 'Fono')
