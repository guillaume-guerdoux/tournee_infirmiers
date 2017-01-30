from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Person(models.Model):
    GENDER_CHOICES = (
        ('1', 'Homme',),
        ('2', 'Femme',),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    postcode = models.IntegerField()
    city = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Office(models.Model):
    address = models.CharField(max_length=255)
    postcode = models.IntegerField()
    city = models.CharField(max_length=255)
    geographical_area = models.IntegerField(default=30)  # Geographical area where nurse can go / in Km
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "Office profile of {0}".format(self.user.username)


class Nurse(Person):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Nurse profile of {0}".format(self.user.username)
