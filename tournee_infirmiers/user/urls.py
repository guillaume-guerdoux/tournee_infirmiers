from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import *
from user import views as user_views

app_name = 'user'
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^register/new_nurse/$', nurse, name='new_nurse'),
    url(r'^register/save_office/$', create_office, name='create_office'),
    url(r'^register/success/$', register_success),
    url(r'^error_login/', user_views.error_login),
    url(r'^account/$', user_views.account, name='account'),
    url(r'^account/nurse/(\d+)$', user_views.nurse_info, name='nurse_info'),
    url(r'^nurse/(\d+)/edit$', user_views.edit_nurse_info, name='edit_nurse_info'),
    url(r'^office/edit/$', user_views.edit_office_info, name='edit_office_info'),
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
    url(r'^logged_out/$', auth_views.logout, {'template_name': 'user/logged_out.html'}, name='logout'),
]
