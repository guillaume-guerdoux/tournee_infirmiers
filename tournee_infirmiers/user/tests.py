from django.test import TestCase
from user.models import Person, Nurse, Patient, Office
from django.contrib.auth.models import User

from datetime import date
# Create your tests here.
class PersonModelTests(TestCase):

	def test_person_user_creation(self):
		user = User.objects.create(username="test@test.fr", first_name = "test",
			last_name = "test")
		user.save()
		person = Person(user = user,
			sex="1", birthdate=date.today(), address="30 allée des Chardons, Paris, France", 
			profile_type = "NURSE")
		person.save()
		user = User.objects.get(username = "test@test.fr")
		self.assertEqual(user.person.sex, "1")
		self.assertEqual(user.person.birthdate, date.today())
		self.assertEqual(user.person.address, "30 allée des Chardons, Paris, France")
		self.assertEqual(user.person.profile_type, "NURSE")

class NurseModelTests(TestCase):

	def test_nurse_creation(self):
		user = User.objects.create(username="test@test.fr", first_name = "test",
			last_name = "test")
		user.save()
		person = Nurse(user = user,
			sex="1", birthdate=date.today(), address="30 allée des Chardons, Paris, France", 
			profile_type = "NURSE")
		person.save()
		user = User.objects.get(username = "test@test.fr")
		self.assertEqual(user.person.nurse.sex, "1")
		self.assertEqual(user.person.nurse.birthdate, date.today())
		self.assertEqual(user.person.nurse.address, "30 allée des Chardons, Paris, France")
		self.assertEqual(user.person.nurse.profile_type, "NURSE")


class PatientModelTests(TestCase):

	def test_nurse_creation(self):
		user = User.objects.create(username="test@test.fr", first_name = "test",
			last_name = "test")
		user.save()
		person = Patient(user = user,
			sex="1", birthdate=date.today(), address="30 allée des Chardons, Paris, France", 
			profile_type = "PATIENT", information = "allergique au doliprane")
		person.save()
		user = User.objects.get(username = "test@test.fr")
		self.assertEqual(user.person.patient.sex, "1")
		self.assertEqual(user.person.patient.birthdate, date.today())
		self.assertEqual(user.person.patient.address, "30 allée des Chardons, Paris, France")
		self.assertEqual(user.person.patient.profile_type, "PATIENT")
		self.assertEqual(user.person.patient.information, "allergique au doliprane")

class OfficeModelTests(TestCase):

	def test_office_creation(self):
	
		office = Office(address="30 allée des Chardons, Paris, France", 
			geographical_area = 40)
		office.save()
		office = Office.objects.get(id = 1)
		self.assertEqual(office.address, "30 allée des Chardons, Paris, France")
		self.assertEqual(office.geographical_area, 40)