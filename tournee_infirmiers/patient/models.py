from django.db import models
from user.models import Person


class Patient(Person):
	information = models.CharField(max_length=255)
	def __str__(self):
		return "Patient profile of {0}".format(self.user.username)
