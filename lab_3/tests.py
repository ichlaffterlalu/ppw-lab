from django.test import TestCase, Client
from django.urls import resolve
from .views import index
from .models import Diary
from django.utils import timezone

import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

# Create your tests here.
class Lab3Test(TestCase):
	def test_lab_3_url_is_exist(self):
		response = client_main.get('/lab-3/')
		self.assertEqual(response.status_code,200)

	def test_lab_3_using_to_do_list_template(self):
		response = client_main.get('/lab-3/')
		self.assertTemplateUsed(response, 'to_do_list.html')

	def test_lab_3_using_index_func(self):
		found = resolve('/lab-3/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_activity(self):
		#Creating a new activity
		new_activity = Diary.objects.create(date=timezone.now(),activity='Aku mau latihan ngoding deh')
		#Retrieving all available activity
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity,1)

	def test_can_save_a_POST_request(self):
		response = client_main.post('/lab-3/add_activity/', data={'date': '2017-10-12T14:14', 'activity' : 'Maen Dota Kayaknya Enak'})
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity, 1)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lab-3/')
		new_response = client_main.get('/lab-3/')
		html_response = new_response.content.decode('utf8')
		self.assertIn('Maen Dota Kayaknya Enak', html_response)

	def test_can_handle_date_time_errors(self):
		response = client_main.post('/lab-3/add_activity/', data={'date': '99999-10-12T14:14', 'activity' : 'Maen Dota Kayaknya Enak'})
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity, 0)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lab-3/')
		new_response = client_main.get('/lab-3/')
		html_response = new_response.content.decode('utf8')
		self.assertIn('ERROR: Date should be from 0001-01-01T00:00 to 9999-31-12T23:59.', html_response)

	def test_can_handle_empty_activity(self):
		response = client_main.post('/lab-3/add_activity/', data={'date': '2017-10-12T14:14', 'activity' : ''})
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity, 0)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lab-3/')
		new_response = client_main.get('/lab-3/')
		html_response = new_response.content.decode('utf8')
		self.assertIn('ERROR: Activity should not be empty.', html_response)

	def test_can_handle_whitespace_only_activity(self):
		response = client_main.post('/lab-3/add_activity/', data={'date': '2017-10-12T14:14', 'activity' : '\t'})
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity, 0)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lab-3/')
		new_response = client_main.get('/lab-3/')
		html_response = new_response.content.decode('utf8')
		self.assertIn('ERROR: Activity should not be empty.', html_response)