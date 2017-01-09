from django.contrib import admin
from user.models import Person
from user.models import Nurse
from user.models import Office
# Register your models here.
admin.site.register(Person)
admin.site.register(Nurse)
admin.site.register(Office)