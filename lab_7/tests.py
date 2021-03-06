from django.test import TestCase
from django.test import Client
from django.urls import resolve
from unittest import skip
from .views import index, friend_list, friend_detail, friend_list_json, add_friend, delete_friend, validate_npm, find_friend, model_to_dict
from .models import Friend
from .api_csui_helper.csui_helper import get_mahasiswa_list, get_detail_mhs_by_npm

import json
import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	print("\nTesting Lab 7")
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab7UnitTest(TestCase):
	def test_lab_7_url_is_exist(self):
		response = client_main.get('/lab-7/')
		self.assertEqual(response.status_code, 200)
	def test_lab_7_using_index_func(self):
		found = resolve('/lab-7/')
		self.assertEqual(found.func, index)

	def test_lab_7_index_returns_json_if_have_params(self):
		response = client_main.get('/lab-7/?page=1&from=nav')
		json_response = json.loads(response.content)
		self.assertEqual(type(json_response), type(list()))
		self.assertEqual(type(json_response[0]), type(dict()))

	def test_model_can_create_new_friend(self):
		# Creating a new activity
		new_friend = Friend.objects.create(friend_name='Ichlasul Affan', npm='1606895606')
		# Retrieving all available activity
		counting_all_friends = Friend.objects.all().count()
		self.assertEqual(counting_all_friends, 1)

	def test_lab_7_add_friend_url_exists(self):
		found = resolve('/lab-7/add-friend/')
		self.assertEqual(found.func, add_friend)

	def test_lab_7_friend_list_is_exist(self):
		found = resolve('/lab-7/friend-list/')
		response = client_main.get('/lab-7/friend-list/')
		self.assertEqual(found.func, friend_list)
		self.assertEqual(response.status_code, 200)

	def test_lab_7_friend_list_uses_ajax(self):
		obj1 = Friend.objects.create(friend_name='Fanisya Dewi Nusabakti', npm='1706039894')
		obj2 = Friend.objects.create(friend_name='Samuel Tupa Febrian', npm='1606878713')
		obj3 = Friend.objects.create(friend_name='Rachmat Ridwan', npm='1606886974')

		found = resolve('/lab-7/get-friend-list/')
		response = client_main.get('/lab-7/get-friend-list/?start=0&end=10')
		self.assertEqual(found.func, friend_list_json)
		self.assertEqual(response.status_code, 200)

		counting_all_friends = Friend.objects.all().count()
		json_response = json.loads(response.content)
		self.assertEqual(counting_all_friends, len(json_response))
		self.assertEqual(type(json_response[0]), type(str()))

		sample1 = json.loads(json_response[0])
		self.assertEqual(sample1["friend_name"], "Fanisya Dewi Nusabakti")
		self.assertEqual(sample1["npm"], "1706039894")

		response2 = client_main.get('/lab-7/get-friend-list/?start=0&end=2')
		json_response2 = json.loads(response2.content)
		self.assertEqual(len(json_response2), 2)

	def test_lab_7_add_friend_can_add_new_friend(self):
		response = client_main.post('/lab-7/add-friend/', {"name":"Annida Safira Arief", "npm":"1706040050"})
		self.assertEqual(response.status_code, 200)

		response_dict = json.loads(response.content)
		self.assertEqual("Annida Safira Arief", response_dict["friend_name"])
		self.assertIn("1706040050", response_dict["npm"])

		counting_all_friends = Friend.objects.all().count()
		self.assertEqual(counting_all_friends, 1)

	def test_lab_7_find_friend_return_true_if_duplicate(self):
		Friend.objects.create(friend_name='Annida Safira Arief', npm='1706040050')
		Friend.objects.create(friend_name='Annida Safira Arief Butterfield', npm='1706040050')
		self.assertEqual(find_friend("1706040050"), True)

	def test_lab_7_can_access_friend_detail(self):
		found = resolve('/lab-7/friend-detail/')
		self.assertEqual(found.func, friend_detail)

		Friend.objects.create(friend_name='Ichlasul Affan', npm='1606895606')
		response = client_main.get('/lab-7/friend-detail/?npm=1606895606')
		html_response = response.content.decode('utf8')

		self.assertEqual(response.status_code, 200)
		self.assertIn("Ichlasul Affan", html_response)
		self.assertIn("1606895606", html_response)
		self.assertIn('<div id="map">', html_response)

	def test_lab_7_can_access_friend_detail_when_actual_data_unavailable(self):
		Friend.objects.create(friend_name='Dummy', npm='0000000000')
		response = client_main.get('/lab-7/friend-detail/?npm=0000000000')
		html_response = response.content.decode('utf8')

		self.assertEqual(response.status_code, 200)
		self.assertIn("Dummy", html_response)
		self.assertIn("0000000000", html_response)
		self.assertIn("- angkatan -", html_response)

	def test_lab_7_validate_npm_url_exists(self):
		found = resolve('/lab-7/validate-npm/')
		self.assertEqual(found.func, validate_npm)

	def test_lab_7_can_validate_npm_used(self):
		Friend.objects.create(friend_name='Ichlasul Affan', npm='1606895606')

		response = client_main.post('/lab-7/validate-npm/', {"npm":"1606895606", "name":"Rachmat Ridwan"})
		response_dict = json.loads(response.content)
		self.assertEqual(response_dict["is_taken"], True)

	def test_lab_7_can_validate_npm_new(self):
		response = client_main.post('/lab-7/validate-npm/', {"npm":"1706040126", "name":"Giovan Isa Musthofa"})
		response_dict = json.loads(response.content)
		self.assertEqual(response_dict["is_taken"], False)

	def test_lab_7_delete_friend_url_exists(self):
		found = resolve('/lab-7/delete-friend/')
		self.assertEqual(found.func, delete_friend)

	def test_lab_7_delete_friend_empty_returns_false_with_json(self):
		response = client_main.get('/lab-7/delete-friend/?friend_id=999')
		json_response = json.loads(response.content)
		self.assertEqual(json_response["result"], False)

	def test_lab_7_delete_friend_when_exists_returns_true_with_json(self):
		obj1 = Friend.objects.create(friend_name='Annida Safira Arief', npm='1706040050')
		obj2 = Friend.objects.create(friend_name='Samuel Tupa Febrian', npm='1606878713')
		obj3 = Friend.objects.create(friend_name='Rachmat Ridwan', npm='1606886974')

		response = client_main.get('/lab-7/delete-friend/?friend_id='+str(obj2.id))
		json_response = json.loads(response.content)
		self.assertEqual(json_response["result"], True)

		counting_all_friends = Friend.objects.all().count()
		self.assertEqual(counting_all_friends, 2)

	def test_lab_7_returns_login_page_if_not_logged_in(self):
		client = Client()
		response = client.get('/lab-7/')
		self.assertTemplateUsed(response, 'login.html')

		response = client.get('/lab-7/friend-list/')
		self.assertTemplateUsed(response, 'login.html')

		response = client.get('/lab-7/friend-detail/?npm=1606895606')
		self.assertTemplateUsed(response, 'login.html')

		response = client.get('/lab-7/get-friend-list/?start=1&end=2')
		self.assertTemplateUsed(response, 'login.html')

		response = client.post('/lab-7/add-friend/', {'name':'Ichlasul Affan', 'npm':'1606895606'})
		self.assertTemplateUsed(response, 'login.html')

		response = client.get('/lab-7/delete-friend/?npm=1606895606')
		self.assertTemplateUsed(response, 'login.html')

		response = client.post('/lab-7/validate-npm/', {'npm':'1606895606'})
		self.assertTemplateUsed(response, 'login.html')