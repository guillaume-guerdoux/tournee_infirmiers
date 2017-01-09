from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class HomeTests(TestCase):

	def test_home_view(self):
		# ---------------------Verifie qu'on est bien dans la home----------------
		response = self.client.get(reverse('home:home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Votre tournée n'aura jamais été aussi rapide")