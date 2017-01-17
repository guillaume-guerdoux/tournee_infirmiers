from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from user import views as user_views

app_name = 'user'
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^register/new_nurse/$', nurse, name='new_nurse'),
    url(r'^register/success/$', register_success),
    url(r'^error_login/', user_views.error_login),
    url(r'^compte/$', user_views.account, name='account'),
    url(r'^user/edit/$', user_views.edit_self_info, name='edit_self_info'),
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^office_login/$', auth_views.login, {'template_name': 'user/office_login.html'}, name='office_login'),
    url(r'^logged_out/$', auth_views.logout, {'template_name': 'user/logged_out.html'}, name='logout'),
]
