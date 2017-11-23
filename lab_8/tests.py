from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

# Create your tests here.
class Lab8UnitTest(TestCase):
	def test_lab_8_url_is_exist(self):
		response = Client().get('/lab-8/')
		self.assertEqual(response.status_code, 200)

	def test_lab_8_using_index_func(self):
		found = resolve('/lab-8/')
		self.assertEqual(found.func, index)