from django.test import TestCase
from django.test import Client
from django.urls import resolve
from django.http import HttpRequest
from .views import index, about_me, landing_page_content
# Create your tests here.

class Lab4UnitTest(TestCase):
	def test_lab_4_url_is_exist(self):
		response = Client().get('/lab-4/')
		self.assertEqual(response.status_code, 200)

	def test_about_me_more_than_6(self):
	   self.assertTrue(len(about_me) >= 6)

	def test_lab4_using_index_func(self):
		found = resolve('/lab-4/')
		self.assertEqual(found.func, index)

	def test_landing_page_is_completed(self):
		request = HttpRequest()
		response = index(request)
		html_response = response.content.decode('utf8')

		#Checking whether have Bio content
		self.assertIn(landing_page_content, html_response)

		#Chceking whether all About Me Item is rendered
		for item in about_me:
			self.assertIn(item,html_response)      
