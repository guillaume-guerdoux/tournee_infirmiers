from django.test import TestCase

#MODELS
from user.models import Nurse
from availability.models import AvailabilityGroup, Availability
from django.contrib.auth.models import User

from datetime import date, datetime, timedelta
# FUNCTIONAL TESTS
from user.function_test import UserCreationTests
# Create your tests here.


class AvailabilityModelTests(TestCase):

	def test_unique_availability_creation(self):
		response = UserCreationTests().create_nurse("test@test.fr", 'test', 
			'test', '1', date.today(), '30 allée des Chardons, Paris, France')
		nurse = Nurse.objects.get(user__username = "test@test.fr")
		availability_group = AvailabilityGroup(nurse = nurse, frequency = "U")
		availability_group.save()

		availability = Availability(start_date = datetime(year = 2017,
			month = 3, day = 20, hour = 9, minute = 30), duration = timedelta(hours = 6), 
			availability_group = availability_group)
		availability.save()

		availability = Availability.objects.get(pk = 1)
		nurse = Nurse.objects.get(pk = 1)
		availability_group = AvailabilityGroup.objects.get(pk = 1)

		self.assertEqual(availability_group.nurse, nurse)
		self.assertEqual(availability_group.frequency, "U")
		self.assertEqual(availability.start_date.replace(tzinfo=None), datetime(year = 2017,
			month = 3, day = 20, hour = 9, minute = 30))
		self.assertEqual(availability.duration, timedelta(hours = 6))
		self.assertEqual(availability.availability_group, availability_group)

	def test_multiple_availability_creation(self):
		response = UserCreationTests().create_nurse("test@test.fr", 'test', 
			'test', '1', date.today(), '30 allée des Chardons, Paris, France')
		nurse = Nurse.objects.get(user__username = "test@test.fr")
		availability_group = AvailabilityGroup(nurse = nurse, frequency = "D")
		availability_group.save()

		availability = Availability(start_date = datetime(year = 2017,
			month = 3, day = 20, hour = 9, minute = 30), duration = timedelta(hours = 6), 
			availability_group = availability_group)
		second_availability = Availability(start_date = datetime(year = 2017,
			month = 3, day = 20, hour = 9, minute = 30) + timedelta(days = 1), duration = timedelta(hours = 6), 
			availability_group = availability_group)

		availability_group.save()
		availability.save()
		second_availability.save()

		availability = Availability.objects.get(pk = 1)
		nurse = Nurse.objects.get(pk = 1)
		availability_group = AvailabilityGroup.objects.get(pk = 1)
		self.assertEqual(availability_group.nurse, nurse)
		self.assertEqual(availability_group.frequency, "D")
		self.assertEqual(availability.start_date.replace(tzinfo=None), datetime(year = 2017,
			month = 3, day = 20, hour = 9, minute = 30))
		self.assertEqual(availability.duration, timedelta(hours = 6))
		self.assertEqual(availability.availability_group, availability_group)

		availability = Availability.objects.get(pk = 2)
		nurse = Nurse.objects.get(pk = 1)
		availability_group = AvailabilityGroup.objects.get(pk = 1)
		self.assertEqual(availability_group.nurse, nurse)
		self.assertEqual(availability_group.frequency, "D")
		self.assertEqual(availability.start_date.replace(tzinfo=None), datetime(year = 2017,
			month = 3, day = 21, hour = 9, minute = 30))
		self.assertEqual(availability.duration, timedelta(hours = 6))
		self.assertEqual(availability.availability_group, availability_group)
