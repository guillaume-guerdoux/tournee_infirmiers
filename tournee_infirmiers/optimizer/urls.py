from django.conf.urls import url
from optimizer import views as optimizer_views

from . import views

app_name = 'optimizer'
urlpatterns = [
    url(r'^optimize/$', optimizer_views.optimize, name="optimize"),
]
