from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, landing_page_content, mhs_name
from django.http import HttpRequest
from unittest import skip

# Create your tests here.
class Lab2AddonUnitTest(TestCase):

    def test_lab_2_addon_url_is_exist(self):
        response = Client().get('/lab-2-addon/')
        self.assertEqual(response.status_code, 200)

    def test_root_url_now_is_using_index_page_from_lab_2(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 301)
        self.assertRedirects(response,'/lab-2/',301,200)

    def test_lab2_addon_using_index_func(self):
        found = resolve('/lab-2-addon/')
        self.assertEqual(found.func, index)

    def test_lab2_addon_bio_dict(self):
        # Check whether bio_dict is not None Object
        self.assertIsNotNone(bio_dict)

        # Check whether bio_dict entry is less than 3 items
        self.assertTrue(len(bio_dict) >= 3)

        # Checking all element in family member
        for bio in bio_dict:
            # Name cannot be None
            self.assertIsNotNone(bio['subject'])
            self.assertIsNotNone(bio['value'])

            # Name cannot be integer
            self.assertIsNot(type(bio['value']), type(8))

    def test_lab2_addon_bio_shown_in_page(self):
        request = HttpRequest()
        response = index(request)
        html_response = response.content.decode('utf8')

        # Checking all family member is shown in page
        for bio in bio_dict:
            self.assertIn('<td class="subject">' + bio['subject'] + '</td>', html_response)
            self.assertIn('<td class="value">' + bio['value'] + '</td>', html_response)
