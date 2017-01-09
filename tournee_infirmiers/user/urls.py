from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views as user_views

app_name = 'user'
urlpatterns = [
    url(r'^error_login/', user_views.error_login),
    url(r'^compte/$', user_views.account, name='account'),
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^office_login/$', auth_views.login, {'template_name': 'user/office_login.html'}, name='office_login'),
    url(r'^logged_out/$', auth_views.logout, {'template_name': 'user/logged_out.html'}, name='logout'),
]
