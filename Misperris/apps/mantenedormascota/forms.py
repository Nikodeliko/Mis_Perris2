from django import forms

from apps.mantenedormascota.models import Perro

class PerroForm(forms.ModelForm):
	class Meta:
		model = Perro

		fields = [
			'nombre',
			'raza',
			'descripcion',
			'estado',
		]
		labels = {
			'nombre': 'Nombre',
			'raza': 'Raza',
			'descripcion': 'Descripcion',
			'estado': 'Estado',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'raza': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
		}	