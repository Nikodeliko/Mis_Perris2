from django.conf.urls import url
from apps.usuario.views import *
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^vista2', PerroList.as_view(), name='vista2'),
]
