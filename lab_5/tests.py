import time
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_todo
from .models import Todo
from .forms import Todo_Form

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import os
import environ

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	print("\nTesting Lab 5")
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab5UnitTest(TestCase):
	def test_lab_5_url_is_exist(self):
		response = client_main.get('/lab-5/')
		self.assertEqual(response.status_code, 200)

	def test_lab5_using_index_func(self):
		found = resolve('/lab-5/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_todo(self):
		# Creating a new activity
		new_activity = Todo.objects.create(title='mengerjakan lab ppw', description='mengerjakan lab_5 ppw')

		# Retrieving all available activity
		counting_all_available_todo = Todo.objects.all().count()
		self.assertEqual(counting_all_available_todo, 1)

	def test_form_todo_input_has_placeholder_and_css_classes(self):
		form = Todo_Form()
		self.assertIn('class="todo-form-input', form.as_p())
		self.assertIn('id="id_title"', form.as_p())
		self.assertIn('class="todo-form-textarea', form.as_p())
		self.assertIn('id="id_description', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = Todo_Form(data={'title': '', 'description': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
			form.errors['description'],
			["Please fill the description with real thing."]
		)
		self.assertEqual(
			form.errors['title'],
			["Please fill the title with real thing."]
		)

	def test_lab5_post_success_and_render_the_result(self):
		test = 'Anonymous'
		response_post = client_main.post('/lab-5/add_todo', {'title': test, 'description': test})
		self.assertEqual(response_post.status_code, 302)

		response= client_main.get('/lab-5/')
		html_response = response.content.decode('utf8')
		self.assertIn(test, html_response)

	def test_lab5_post_error_and_render_the_result(self):
		test = 'Anonymous'
		response_post = client_main.post('/lab-5/add_todo', {'title': '', 'description': ''})
		self.assertEqual(response_post.status_code, 302)

		response= client_main.get('/lab-5/')
		html_response = response.content.decode('utf8')
		self.assertNotIn(test, html_response)

	def test_lab5_can_delete_todo(self):
		previous_count = Todo.objects.all().count()
		response_post = client_main.post('/lab-5/add_todo', {'title': 'bener', 'description': 'bener'})

		idPost = Todo.objects.all()[0].id

		response=client_main.get('/lab-5/delete_todo?id=' + str(idPost), follow=True)

		counting_all_available_todo = Todo.objects.all().count()
		self.assertEqual(counting_all_available_todo, previous_count)

		html_response = response.content.decode('utf8')
		self.assertIn("Todo has been deleted.", html_response)

	def test_lab5_handled_error_delete_todo(self):
		response=client_main.get('/lab-5/delete_todo?id=10000000000000', follow=True)
		html_response = response.content.decode('utf8')
		self.assertIn("The todo does not exist.", html_response)


class Lab5FunctionalTest(TestCase):
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument('--dns-prefetch-disable')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('disable-gpu')
		try: self.selenium  = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
		except: self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
		super(Lab5FunctionalTest, self).setUp()

		# Login
		self.root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
		self.env = environ.Env(DEBUG=(bool, False),)
		environ.Env.read_env('.env')

		self.selenium.get('http://127.0.0.1:8000/lab-5/')
		username = self.selenium.find_element_by_id("username")
		password = self.selenium.find_element_by_id("password")

		username.send_keys(self.env("SSO_USERNAME"))
		password.send_keys(self.env("SSO_PASSWORD"))

		self.selenium.find_element_by_id("submit").click()

		self.selenium.get('http://127.0.0.1:8000/lab-5/')

	def tearDown(self):
		self.selenium.quit()
		super(Lab5FunctionalTest, self).tearDown()

	def test_input_todo(self):
		selenium = self.selenium
		# Opening the link we want to test
		selenium.get('http://127.0.0.1:8000/lab-5/')
		# find the form element
		title = selenium.find_element_by_id('id_title')
		description = selenium.find_element_by_id('id_description')

		submit = selenium.find_element_by_id('submit')

		# Fill the form with data
		title.send_keys('Mengerjakan Lab PPW')
		description.send_keys('Lab kali ini membahas tentang CSS dengan penggunaan Selenium untuk Test nya')

		# submitting the form
		submit.send_keys(Keys.RETURN)

		# check if there's a success message
		self.assertIn('Todo has been created.', selenium.page_source)

	def test_delete_todo(self):
		selenium = self.selenium
		# Opening the link we want to test
		self.test_input_todo()
		selenium.get('http://127.0.0.1:8000/lab-5/')

		# find the delete button
		todo_item = selenium.find_element_by_css_selector("div[id*='todo-']")
		delete_button = selenium.find_element_by_css_selector("a[href*='/lab-5/delete_todo?id=']")

		# click the delete button
		hover = ActionChains(selenium).move_to_element(todo_item)
		hover.perform()
		time.sleep(1)
		delete_button.click()

		# check if there's a success message
		self.assertIn('Todo has been deleted.', selenium.page_source)