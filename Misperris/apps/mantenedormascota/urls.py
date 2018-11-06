from django.conf.urls import url
from apps.mantenedormascota.views import index, PerroList, PerroCreate, PerroUpdate, PerroDelete, PerroSearch

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^agregar$', PerroCreate.as_view(), name='agregar_perro'),
    url(r'^listar', PerroList.as_view(), name='listar_perro'),
    url(r'^modificar/(?P<pk>\d+)/$', PerroUpdate.as_view(), name='actualizar_perro'),
    url(r'^eliminar/(?P<pk>\d+)/$', PerroDelete.as_view(), name='eliminar_perro'),
    url(r'^buscar$', PerroSearch.as_view(), name='buscar_perro'),
]
