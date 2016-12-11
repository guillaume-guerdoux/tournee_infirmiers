from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
