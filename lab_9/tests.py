from django.test import TestCase
from django.test import Client
from django.urls import resolve
import requests
from .views import index, set_data_for_session, profile, cookie_login, cookie_auth_login, cookie_profile, cookie_clear, my_cookie_auth, is_login, add_session_item, del_session_item, clear_session_item
from .api_enterkomputer import get_drones, get_soundcards, get_opticals

from praktikum.csui_login_helper import get_access_token, get_client_id, verify_user, get_data_user, API_VERIFY_USER, API_MAHASISWA

import json
import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab9UnitTest(TestCase):
	def test_lab_9_url_is_exist_and_redirects_when_logged_in(self):
		response = client_main.get('/lab-9/')
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response,'/lab-9/profile/',302,200)

	def test_lab_9_url_is_exist_not_redirect_when_not_logged_in(self):
		response = Client().get('/lab-9/')
		self.assertEqual(response.status_code, 200)

	def test_lab_9_using_index_func(self):
		found = resolve('/lab-9/')
		self.assertEqual(found.func, index)

	def test_root_url_now_is_using_index_page_from_lab_9(self):
		response = client_main.get('/')
		self.assertEqual(response.status_code, 301)
		self.assertRedirects(response,'/lab-9/',301,302)

	def test_lab_9_profile_url_is_exist(self):
		response = client_main.get('/lab-9/profile/')
		self.assertEqual(response.status_code, 200)

		found = resolve('/lab-9/profile/')
		self.assertEqual(found.func, profile)

	def test_lab_9_profile_rendered_successfully_when_logged_in(self):
		response = client_main.get('/lab-9/profile/')
		html_response = response.content.decode('utf8')
		self.assertIn("[Session] Profile", html_response)

	def test_lab_9_can_operate_favorite_items_in_session(self):
		# initialize
		drones = json.loads(get_drones().content)
		soundcards = json.loads(get_soundcards().content)
		opticals = json.loads(get_opticals().content)

		# add (2 drones, 1 soundcard, 2 opticals)
		response = client_main.get('/lab-9/add_session_item/drones/'+drones[0]["id"]+"/", follow=True)
		response = client_main.get('/lab-9/add_session_item/drones/'+drones[5]["id"]+"/", follow=True)
		response = client_main.get('/lab-9/add_session_item/soundcards/'+soundcards[2]["id"]+"/", follow=True)
		response = client_main.get('/lab-9/add_session_item/opticals/'+opticals[2]["id"]+"/", follow=True)
		response = client_main.get('/lab-9/add_session_item/opticals/'+opticals[3]["id"]+"/", follow=True)
		response = client_main.get('/lab-9/add_session_item/opticals/'+opticals[2]["id"]+"/", follow=True)

		# delete (1 drone, 1 soundcard, 1 optical)
		response = client_main.get('/lab-9/del_session_item/drones/'+drones[0]["id"]+"/", follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus item drones dari favorite', html_response)
		response = client_main.get('/lab-9/del_session_item/soundcards/'+soundcards[2]["id"]+"/", follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus item soundcards dari favorite', html_response)
		response = client_main.get('/lab-9/del_session_item/opticals/'+opticals[2]["id"]+"/", follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus item opticals dari favorite', html_response)

		# reset favorite drones
		response = client_main.get('/lab-9/clear_session_item/drones/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus session: favorite drones', html_response)

		# reset favorite drones when it's empty

		response = client_main.get('/lab-9/clear_session_item/drones/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Favorite drones kosong', html_response)

		# reset favorite soundcards
		response = client_main.get('/lab-9/clear_session_item/soundcards/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus session: favorite soundcards', html_response)

		# reset favorite soundcards when it's empty
		response = client_main.get('/lab-9/clear_session_item/soundcards/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Favorite soundcards kosong', html_response)

		# reset favorite opticals
		response = client_main.get('/lab-9/clear_session_item/opticals/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Berhasil hapus session: favorite opticals', html_response)

		# reset favorite opticals when it's empty
		response = client_main.get('/lab-9/clear_session_item/opticals/', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn('Favorite opticals kosong', html_response)

	def test_login_cookie_page(self):
		# test if template is correct
		response = client_main.get('/lab-9/cookie/login/')
		self.assertTemplateUsed(response, 'lab_9/cookie/login.html')

		# test for redirect when authentication
		response = client_main.get('/lab-9/cookie/auth_login/')
		self.assertEqual(response.status_code, 302)

		# test for redirect when not logged in
		response = client_main.get('/lab-9/cookie/profile/')
		self.assertEqual(response.status_code, 302)

		# test for wrong username and password
		response = client_main.post('/lab-9/cookie/auth_login/', {'username': 'ichlasul.affan', 'password': 'SayaSendiri'})
		response = client_main.get('/lab-9/cookie/login/')
		html_response = response.content.decode('utf8')
		self.assertIn('Username atau Password Salah', html_response)

		# test login on valid cookie
		response = client_main.post('/lab-9/cookie/auth_login/', {'username': 'utest', 'password': 'ptest'})
		response = client_main.get('/lab-9/cookie/login/')
		response = client_main.get('/lab-9/cookie/profile/')
		self.assertTemplateUsed(response, 'lab_9/cookie/profile.html')

		# test on hack handling
		response = client_main.get('/lab-9/cookie/profile/')
		response.client.cookies['user_login'] = '32143215'
		response = client_main.get('/lab-9/cookie/profile/')
		self.assertTemplateUsed(response, 'lab_9/cookie/login.html')

		# test logout halaman cookie
		response = client_main.post('/lab-9/cookie/auth_login/', {'username': 'utest', 'password': 'ptest'})
		response = client_main.get('/lab-9/cookie/clear/')
		self.assertEqual(response.status_code, 302)

class ApiEnterkomputerUnitTest(TestCase):
	def test_drones_api(self):
		response = requests.get('https://www.enterkomputer.com/api/product/drone.json')
		self.assertEqual(response.json(),get_drones().json())

	def test_soundcards_api(self):
		response = requests.get('https://www.enterkomputer.com/api/product/soundcard.json')
		self.assertEqual(response.json(),get_soundcards().json())

	def test_optical_api(self):
		response = requests.get('https://www.enterkomputer.com/api/product/optical.json')
		self.assertEqual(response.json(),get_opticals().json())

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