from django.conf.urls import url

from . import views

app_name = 'patient'
urlpatterns = [
    url(r'patient/new/$', views.patient, name="new_patient"),
    url(r'patient/(\d+)$', views.patient_info, name="patient_info"),
    url(r'patient/list/$', views.patient_list, name="patient_list"),
]
