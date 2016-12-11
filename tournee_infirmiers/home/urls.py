from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.home, name='root'),
    url(r'^home/', views.home, name='home')
]
