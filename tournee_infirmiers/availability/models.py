from django.db import models

from user.models import Nurse
# Create your models here.
class AvailabilityGroup(models.Model):
	FREQUENCY = (
		('U', 'Unique',),
		('D', 'Tous les jours',),
		('W', 'Toutes les semaines',),
	)
	nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
	frequency = models.CharField(max_length=1, choices=FREQUENCY)
	def __str__(self):
		return "Group"
		
class Availability(models.Model):
	start_date = models.DateTimeField()
	duration = models.DurationField()
	availability_group = models.ForeignKey(AvailabilityGroup, on_delete=models.CASCADE)


