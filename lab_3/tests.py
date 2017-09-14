from django.test import TestCase, Client
from django.urls import resolve
from .views import index
from .models import Diary
from django.utils import timezone

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
		
	def test_model_can_create_new_activity(self):
		#Creating a new activity
		new_activity = Diary.objects.create(date=timezone.now(),activity='Aku mau latihan ngoding deh')
		#Retrieving all available activity
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity,1)
	def test_can_save_a_POST_request(self):
		response = self.client.post('/lab-3/add_activity/', data={'date': '2017-10-12T14:14', 'activity' : 'Maen Dota Kayaknya Enak'})
		counting_all_available_activity = Diary.objects.all().count()
		self.assertEqual(counting_all_available_activity, 1)
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/lab-3/')
		new_response = self.client.get('/lab-3/')
		html_response = new_response.content.decode('utf8')
		self.assertIn('Maen Dota Kayaknya Enak', html_response)
