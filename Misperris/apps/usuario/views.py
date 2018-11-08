from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView

from apps.mantenedormascota.forms import PerroForm
from apps.mantenedormascota.models import Perro

# Create your views here.
def index(request):
	return render(request, 'usuario/index.html')

class PerroList(ListView):
	model = Perro
	template_name = 'usuario/vista2.html'
	paginate_by = 3
