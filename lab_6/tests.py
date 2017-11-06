from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

# Create your tests here.
# Create your tests here.
class Lab6UnitTest(TestCase):
	def test_lab_6_url_is_exist(self):
		response = Client().get('/lab-6/')
		self.assertEqual(response.status_code, 200)

	def test_lab_6_using_index_func(self):
		found = resolve('/lab-6/')
		self.assertEqual(found.func, index)

	def test_root_url_now_is_using_index_page_from_lab_4(self):
		response = Client().get('/')
		self.assertEqual(response.status_code, 301)
		self.assertRedirects(response,'/lab-4/',301,200)