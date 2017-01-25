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

    def __str__(self):
        return 'Disponiblité {0} le {1} {2} {3} à partir de {4}:{5}:{6} durant {7}'.format(
            self.availability_group.frequency,
            self.start_date.day, self.start_date.month, self.start_date.year,
            self.start_date.hour, self.start_date.minute, self.start_date.second,
            self.duration)
