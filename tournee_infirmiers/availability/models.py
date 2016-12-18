from django.db import models

from user.models import Nurse
# Create your models here.
class AvailabilityGroup(models.Model):
	def __str__(self):
		return "Group"
		
class Availability(models.Model):
	nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	duration = models.DurationField()
	availability_group = models.ForeignKey(AvailabilityGroup, on_delete=models.CASCADE)


