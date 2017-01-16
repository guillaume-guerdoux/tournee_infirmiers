from django.db import models
from patient.models import Patient


class Need(models.Model):
    need_string = models.CharField(max_length=4)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
