from django.conf.urls import url
from . import views


app_name = 'event'
urlpatterns = [
    url(r'^patient/(\d+)/add_need/', views.add_need, name='add_need'),
    url(r'^appointment/(\d+)$', views.appointment_detail, name='appointment_detail')
]
