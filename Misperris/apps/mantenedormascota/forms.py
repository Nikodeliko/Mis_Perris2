from django import forms

from apps.mantenedormascota.models import Perro

class PerroForm(forms.ModelForm):
	class Meta:
		model = Perro

		fields = [
			"nombre",
			"raza",
			"descripcion",
			"estado",
			"fotografia",
		]
		labels = {
			'nombre': 'Nombre',
			'raza': 'Raza',
			'descripcion': 'Descripcion',
			'estado': 'Estado',
			'fotografia': 'Sube la foto del perro',
		}
		widgets = {
			'fotografia': forms.FileInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'raza': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.TextInput(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control'}),
		}
