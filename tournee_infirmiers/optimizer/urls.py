from django.conf.urls import url
from optimizer import views as optimizer_views

from . import views

app_name = 'optimizer'
urlpatterns = [
    url(r'^optimize/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)$', optimizer_views.optimize, name="optimize"),
]
