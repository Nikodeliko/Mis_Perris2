from django.conf.urls import url
from Index.views import *

urlpatterns = [
	url(r'^Index/$', PerrisList.as_view(), name='Index')
]