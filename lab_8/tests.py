from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab8UnitTest(TestCase):
	def test_lab_8_url_is_exist(self):
		response = client_main.get('/lab-8/')
		self.assertEqual(response.status_code, 200)

	def test_lab_8_using_index_func(self):
		found = resolve('/lab-8/')
		self.assertEqual(found.func, index)