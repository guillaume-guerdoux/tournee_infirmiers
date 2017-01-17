from django.db import models
from user.models import Person


class Patient(Person):
	information = models.CharField(max_length=255)
	def __str__(self):
		return ("{0} ".format(self.first_name) + "{0}".format(self.last_name))
