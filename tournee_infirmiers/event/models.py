from django.db import models
from patient.models import Patient
from django.core.exceptions import ValidationError

#def validate_duration(duration, duration_heal):
    #if duration < duration_heal:
        #raise ValidationError(u'The duration of the heal %s is greater than the availability duration of the patient' % duration_heal)

class Need(models.Model):
    need_string = models.CharField(max_length=4)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    duration_heal=models.DurationField()