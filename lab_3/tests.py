from django.test import TestCase, Client
from django.urls import resolve
from .views import index

# Create your tests here.
class Lab3Test(TestCase):
	def test_lab_3_url_is_exist(self):
		response = Client().get('/lab-3/')
		self.assertEqual(response.status_code,200)

	def test_lab_3_using_to_do_list_template(self):
		response = Client().get('/lab-3/')
		self.assertTemplateUsed(response, 'to_do_list.html')

	def test_lab_3_using_index_func(self):
		found = resolve('/lab-3/')
		self.assertEqual(found.func, index)
