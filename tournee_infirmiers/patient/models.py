from django.db import models
from user import models as user_models


class Patient(user_models.Person):
	information = models.CharField(max_length=255)
	def __str__(self):
		return "Patient profile of {0}".format(self.user.username)
