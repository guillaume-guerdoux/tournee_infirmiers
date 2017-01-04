# PARAMETER FOR TESTCASE 
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
#MODELS
from django.contrib.auth.models import User
from user.models import Nurse

class UserCreationTests(TestCase):

	def create_nurse(self, email, password, first_name, last_name, sex,
		birthdate, address):
		user = User.objects.create(username=email, password=password,
		 first_name = first_name, last_name = last_name)
		user.save()
		person = Nurse(user = user,
			sex=sex, birthdate=birthdate, address=address, 
			profile_type = "NURSE")
		person.save()

class UserLoginTests(TestCase):

	def login(self, client, username, password):
		response = client.post('/login/', {'username': 'test@test.fr', 'password': 'test'})