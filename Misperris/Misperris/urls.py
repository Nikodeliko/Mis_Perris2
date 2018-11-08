"""Misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from Index import views


urlpatterns = [
    url(r'^$',views.plantilla_cargada),
    path('admin/', admin.site.urls),
    url(r'^Usuario-registrado/$',views.gestionarUsuarios,name="gestionarUsuarios"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^registrar/$',views.agregarusuario,name="agregarusuario"),
    url(r'^mantenedor/',include(('apps.mantenedormascota.urls', 'mantenedor'), namespace='mantenedor')),
    url(r'^vista-adopcion/', include(('apps.usuario.urls', 'usuario'), namespace='usuario')),

    #Recuperar contraseña

    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="password_reset"),
    url(r'^password-reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    url(r'^password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    url(r'^password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
