from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'patient/new/$', views.patient, name="new_patient"),
]