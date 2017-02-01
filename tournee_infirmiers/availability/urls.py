from django.conf.urls import url

from . import views

app_name = 'availability'
urlpatterns = [
    url(r'^availability/list$', views.manage_availabilities, name='manage_availability'),
    url(r'^availability/new/(\d+)$', views.add_availability, name='add_availability'),
    url(r'^availability/choose_nurse$', views.choose_nurse, name='nurse_choice'),
    url(r'^ajax/remove_unique_availability$', views.remove_unique_availability, name='remove_unique_availability'),
    url(r'^ajax/remove_repeatly_availability_only_this_one$',
        views.remove_repeatly_availability_only_this_one, name='remove_repeatly_availability_only_this_one'),
    url(r'^ajax/remove_repeatly_availability_all$',
        views.remove_repeatly_availability_all, name='remove_repeatly_availability_all'),
]
