from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from apps.mantenedormascota.forms import PerroForm
from apps.mantenedormascota.models import Perro
# Create your views here.

def index(request):
	return render(request, 'mantenedor/index.html')

class PerroList(ListView):
	model = Perro
	template_name = 'mantenedor/listar_perro.html'
	paginate_by = 5

class PerroCreate(CreateView):
	model = Perro
	form_class = PerroForm	
	template_name = 'mantenedor/agregar_perro.html'
	success_url = reverse_lazy('mantenedor:listar_perro')

class PerroUpdate(UpdateView):
	model = Perro
	form_class = PerroForm	
	template_name = 'mantenedor/modificar_perro.html'
	success_url = reverse_lazy('mantenedor:listar_perro')

class PerroDelete(DeleteView):
	model = Perro
	template_name = 'mantenedor/eliminar_perro.html'
	success_url = reverse_lazy('mantenedor:listar_perro')

class PerroSearch(TemplateView):
	def post(self, request, *args, **kwargs):
		buscar = request.POST['buscando']
		perro = Perro.objects.filter(nombre=buscar)
		return render(request, 'mantenedor/buscar_perro.html', {'perro':perro})
		
