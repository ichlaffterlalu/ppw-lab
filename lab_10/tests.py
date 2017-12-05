from django.test import TestCase
from django.test import Client
from django.urls import resolve, reverse
from django.http import HttpRequest
import requests
from .views import *
from .omdb_api import get_detail_movie, create_json_from_dict, search_movie, API_KEY

import os
import environ
import json

# Create your tests here.
client_main = Client()
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env('.env')

def setUpModule():
	print("\nTesting Lab 10")
	client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})

class Lab10UnitTest(TestCase):
    def test_lab_10_url_is_exist(self):
        response = client_main.get('/lab-10/')
        self.assertEqual(response.status_code, 200)

    def test_root_url_now_is_using_index_page_from_lab_10(self):
        response = client_main.get('/')
        self.assertEqual(response.status_code, 301)
        self.assertRedirects(response,'/lab-10/',301,200)

    def test_lab_10_using_index_func(self):
        found = resolve('/lab-10/')
        self.assertEqual(found.func, index)

    def test_lab_10_using_right_template(self):
        # if not logged in
        response = Client().get('/lab-10/')
        self.assertTemplateUsed(response, 'login.html')

        # after logged in
        response = client_main.get('/lab-10/')
        self.assertEqual(response.status_code, 200)


    def test_dashboard(self):
        # if user login for the first time in lab 10
        response_post = client_main.post(reverse('auth_login'), {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})
        response_post = client_main.get(reverse('lab-10:dashboard'), follow = True)
        self.assertTemplateUsed(response_post, 'lab_10/dashboard.html')
        # logout
        response_post = client_main.post(reverse('auth_logout'))
        # second time login
        response_post = client_main.post(reverse('auth_login'), {'username': env("SSO_USERNAME"), 'password': env("SSO_PASSWORD")})
        response_post = client_main.get(reverse('lab-10:dashboard'))
        html_response = response_post.content.decode('utf8')
        self.assertIn(env("SSO_USERNAME"),html_response)

    def test_list_movie_page_exist(self):
        response_post = client_main.get(reverse('lab-10:movie_list'))
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/list.html")
        client_main.post('/custom_auth/login/', {"username": env("SSO_USERNAME"), "password": env("SSO_PASSWORD")})
        response_post = client_main.get(reverse('lab-10:movie_list'),{'judul':'It','tahun':'2017'})
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/list.html")

    def test_detail_page(self):
        # test if not logged in
        response_post = Client().get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/detail.html")

        # test after logged in
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/detail.html")

    def test_add_watch_later_and_list_watch_later(self):
        # test with invalid id
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tidakada'}))
        self.assertEqual(response_post.status_code, 302)

        # test when logged in (data saved to database)
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
        self.assertEqual(response_post.status_code, 302)
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Berhasil tambah movie ke Watch Later',html_response)

        # test list_watch_later when logged in (data picked from database)
        response_post = client_main.get(reverse('lab-10:list_watch_later'))
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/watch_later.html")
        html_response = response_post.content.decode('utf8')
        self.assertIn('It',html_response)

        # test when adding with id which already added before
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
        self.assertEqual(response_post.status_code, 302)
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Movie already exist on DATABASE! Hacking detected!',html_response)

        # add one more movie
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt3874544'}))
        self.assertEqual(response_post.status_code, 302)
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt3874544'}))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Berhasil tambah movie ke Watch Later',html_response)

        # test if logged out
        response_post = client_main.get(reverse('auth_logout'))

        # test when adding without login (data saved to session)
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}), follow = True)
        self.assertEqual(response_post.status_code, 200)
        html_response = response_post.content.decode('utf8')
        self.assertIn('Berhasil tambah movie ke Watch Later',html_response)

        # test list_watch_later without login (data saved to session)
        response_post = client_main.get(reverse('lab-10:list_watch_later'))
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post,"lab_10/movie/watch_later.html")
        html_response = response_post.content.decode('utf8')
        self.assertIn('It',html_response)

        # test jika id yang sama ditambahkan kembali secara manual tanpa login
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt1396484'}))
        self.assertEqual(response_post.status_code, 302)
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt1396484'}))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Movie already exist on SESSION! Hacking detected!',html_response)

        # menambahkan satu movie lagi tanpa login
        response_post = client_main.get(reverse('lab-10:add_watch_later', kwargs={'id':'tt4649466'}))
        self.assertEqual(response_post.status_code, 302)
        response_post = client_main.get(reverse('lab-10:movie_detail', kwargs={'id':'tt4649466'}))
        html_response = response_post.content.decode('utf8')
        self.assertIn('Berhasil tambah movie ke Watch Later',html_response)

        # if there are movies exist in session, and user logged in, it will be saved to database
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.post(reverse('auth_login'), {'username': env("SSO_USERNAME"), 'password': env("SSO_PASSWORD")})
        response_post = client_main.get(reverse('lab-10:dashboard'))
        response_post = client_main.get(reverse('lab-10:list_watch_later'))
        self.assertTemplateUsed(response_post,"lab_10/movie/watch_later.html")
        html_response = response_post.content.decode('utf8')
        self.assertIn('It',html_response)

    def test_search_movie_exist(self):
        response_post = client_main.get(reverse('lab-10:api_search_movie', kwargs={'tahun':'-','judul':'It'}))
        self.assertEqual(response_post.status_code, 200)
        response_post = client_main.get(reverse('lab-10:api_search_movie', kwargs={'judul':'-','tahun':'2017'}))
        self.assertEqual(response_post.status_code, 200)
        response_post = client_main.get(reverse('lab-10:api_search_movie', kwargs={'judul':'It','tahun':'2017'}))
        self.assertEqual(response_post.status_code, 200)
        response_post = client_main.get(reverse('lab-10:api_search_movie', kwargs={'judul':'-','tahun':'-'}))
        self.assertEqual(response_post.status_code, 200)

    def test_get_detail_movie(self):
        response = requests.get("http://www.omdbapi.com/?i=tt1396484&apikey="+API_KEY)
        response = response.json()
        response = create_json_from_dict(response)
        self.assertEqual(response,get_detail_movie("tt1396484"))

    def test_search_non_exist_movie(self):
        response = search_movie("asdf","-")
        self.assertEqual(len(response),0)

    def test_search_exist_movie(self):
        response = search_movie("Your Name","2016")
        self.assertTrue(len(response) > 0)