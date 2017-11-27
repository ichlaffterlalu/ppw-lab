from django.test import TestCase
from django.test import Client
from django.urls import resolve
import requests
from .csui_login_helper import get_access_token, get_client_id, verify_user, get_data_user, API_VERIFY_USER, API_MAHASISWA

import json
import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	print("\nTesting CSUI Login Mechanism")
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class CsuiLoginHelperUnitTest(TestCase):
	def test_csui_login_helper_username_and_pass_wrong(self):
		username = "ichlaffterlalu"
		password = "meowmeow"
		self.assertEqual(None, get_access_token(username, password))

	def test_csui_login_helper_verify_function(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		access_token = get_access_token(self.username,self.password)
		parameters = {"access_token": access_token, "client_id": get_client_id()}
		response = requests.get(API_VERIFY_USER, params=parameters)
		result = verify_user(access_token)
		self.assertEqual(result,response.json())

	def test_get_data_user_function(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")

		access_token = get_access_token(self.username,self.password)
		parameters = {"access_token": access_token, "client_id": get_client_id()}

		npm = json.loads(requests.get(API_VERIFY_USER, params=parameters).content)["identity_number"]
		response = requests.get(API_MAHASISWA+npm, params=parameters)

		result = get_data_user(access_token,npm)
		self.assertEqual(result,response.json())

class CustomAuthUnitTest(TestCase):
	def test_login_auth(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = Client().post("/custom_auth/login/", {'username': self.username, 'password': self.password})
		self.assertEqual(response_post.status_code, 302)

	def test_fail_login(self):
		response = Client().post("/custom_auth/login/", {'username': 'ichlaffterlalu', 'password': 'SayaSendiri'}, follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Wrong username or password.', html_response)

	def test_logout_auth(self):
		self.username = env("SSO_USERNAME")
		self.password = env("SSO_PASSWORD")
		response_post = self.client.post("/custom_auth/login/", {'username': self.username, 'password': self.password})
		response = self.client.post("/custom_auth/logout/")
		response = self.client.get('/lab-9/')
		html_response = response.content.decode('utf8')
		self.assertIn('Logout successful. Your session has been removed.', html_response)