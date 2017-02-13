from django.db import models
from patient.models import Patient
from user.models import Nurse
from django.core.exceptions import ValidationError


# def validate_duration(duration, duration_heal):
#    if duration < duration_heal:
#        raise ValidationError(
#           u'The duration of the heal %s is greater than the availability duration of the patient'
#            % duration_heal)

class Need(models.Model):
    ''' Explanation of fields :
        nedd_string : Type of need
        date : date where needs is to be done
        start / end : If need has to be done in a particular time slot, start
        and end are the times where the heal has to be BEGUN
        duration_heal : Duration of the heal'''
    # TODO : Clean function to prevent end from being before start
    need_string = models.CharField(max_length=4)
    date = models.DateField(auto_now=False, auto_now_add=False)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    duration_heal=models.DurationField()


class Appointment(models.Model):
    start = models.DateField(auto_now=False, auto_now_add=False)
    duration = models.DurationField()
    nurse = models.ForeignKey(Nurse)
    need = models.OneToOneField(Need)

    def __str__(self):
        return "Appointment"
