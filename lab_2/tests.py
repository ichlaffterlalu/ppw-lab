from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, landing_page_content, mhs_name

import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
    print("\nTesting Lab 2")
    client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab2UnitTest(TestCase):
    def test_lab_2_url_is_exist(self):
        response = client_main.get('/lab-2/')
        self.assertEqual(response.status_code,200)

    def test_lab2_using_index_func(self):
        found = resolve('/lab-2/')
        self.assertEqual(found.func, index)

    def test_landing_page_content_is_written(self):
        #Content cannot be null
        self.assertIsNotNone(landing_page_content)

        #Content is filled with 30 characters at least
        self.assertTrue(len(landing_page_content) >= 30)

    def test_landing_page_is_completed(self):
        response = client_main.get('/lab-2/')
        html_response = response.content.decode('utf8')
        self.assertIn('Hello, this is '+ mhs_name +'.', html_response)
        self.assertIn(landing_page_content, html_response)