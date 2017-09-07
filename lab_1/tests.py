from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, mhs_name, calculate_age
from django.http import HttpRequest
from datetime import date
import unittest


# Create your tests here.

class Lab1UnitTest(TestCase):

    def test_hello_name_is_exist(self):
        response = Client().get('/lab-1/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/lab-1/')
        self.assertEqual(found.func, index)

    def test_name_is_changed(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertIn('<title>' + mhs_name + '</title>', html_response)
        self.assertIn('<h1>Hello my name is ' + mhs_name + '</h1>', html_response)
        self.assertFalse(len(mhs_name) == 0)


    def test_calculate_age_is_correct(self):
        self.assertEqual(0, calculate_age(date.today().year))
        self.assertEqual(17, calculate_age(2000))
        self.assertEqual(27, calculate_age(1990))


    def test_index_contains_age(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')
        self.assertRegex(html_response, r'<article>I am [0-9]\d+ years old</article>')
