from django.conf.urls import url

from . import views

app_name = 'availability'
urlpatterns = [
	url(r'^dashboard/manage_availability$', views.manage_availability, name='manage_availability'),
]
