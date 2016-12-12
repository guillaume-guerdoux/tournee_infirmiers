from django.conf.urls import url
from . import views


app_name = 'event'
urlpatterns = [
    url(r'^add_need/', views.add_need, name='add_need')
]
