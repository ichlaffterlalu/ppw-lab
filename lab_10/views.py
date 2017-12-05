# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from lab_login.custom_auth import check_login
from .omdb_api import get_detail_movie, search_movie
from .utils import *
response = {}

# Create your views here.

### USER
def index(request):
    print ("#==> masuk index")
    returned = check_login(request, HttpResponseRedirect(reverse('lab-10:dashboard')), response)
    if type(returned) == HttpResponseRedirect: return returned
    else: return render(request, returned, response)

def dashboard(request):
    print ("#==> dashboard")
    if not 'user_login' in request.session.keys():
        return HttpResponseRedirect(reverse('lab-10:index'))
    else:
        set_data_for_session(request)
        kode_identitas = request.session.get('kode_identitas')
        try:
            pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
        except Exception as e:
            pengguna = create_new_user(request)

        movies_id = get_my_movies_from_session(request)
        save_movies_to_database(pengguna, movies_id)
        response['access_token'] = request.session['access_token']
        response['kode_identitas'] = request.session['kode_identitas']
        response['connected'] = True

        html = 'lab_10/dashboard.html'
        return render(request, html, response)


### MOVIE : LIST and DETAIL
def movie_list(request):
    if request.session.get('user_login'):
        response['user_login'] = request.session.get('user_login')
    else:
        response.pop('user_login', None)

    judul, tahun = get_parameter_request(request)
    urlDataTables = "/lab-10/api/movie/" + judul + "/" + tahun
    jsonUrlDT = json.dumps(urlDataTables)
    response['jsonUrlDT'] = jsonUrlDT
    response['judul'] = judul
    response['tahun'] = tahun

    get_data_session(request)

    html = 'lab_10/movie/list.html'
    return render(request, html, response)

def movie_detail(request, id):
    print ("MOVIE DETAIL = ", id)
    response['id'] = id
    if request.session.get('user_login'):
        is_added = check_movie_in_database(request, id)
    else:
        is_added = check_movie_in_session(request, id)

    response['added'] = is_added
    response['movie'] = get_detail_movie(id)
    html = 'lab_10/movie/detail.html'
    return render(request, html, response)

### WATCH LATER : ADD and LIST
def add_watch_later(request, id):
    print ("ADD WL => ", id)
    msg = "Berhasil tambah movie ke Watch Later"
    check_exist = get_detail_movie(id)
    if str(check_exist["response"])=="b'True'" :
    	if request.session.get('user_login'):
    		print ("TO DB")
    		is_in_db = check_movie_in_database(request, id)
    		if not is_in_db:
    			add_item_to_database(request, id)
    		else:
    			msg = "Movie already exist on DATABASE! Hacking detected!"
    	else:
    		print ("TO SESSION")
    		is_in_ssn = check_movie_in_session(request, id)
    		if not is_in_ssn:
    			add_item_to_session(request, id)
    		else:
    			msg = "Movie already exist on SESSION! Hacking detected!"
    else:
    	msg = "Movie tidak dapat ditambahkan : id tidak ditemukan"
    	messages.error(request, msg)
    	return HttpResponseRedirect(reverse('lab-10:index'))
    messages.success(request, msg)
    return HttpResponseRedirect(reverse('lab-10:movie_detail', args=(id,)))

def list_watch_later(request):
    #  Implement this function by yourself
    get_data_session(request)
    moviesku = []
    if request.session.get('user_login'):
        moviesku = get_my_movies_from_database(request)
        response['user_login'] = request.session.get('user_login')
    else:
        response.pop('user_login', None)
        moviesku = get_my_movies_from_session(request)

    watch_later_movies = get_list_movie_from_api(moviesku)
    response['watch_later_movies'] = watch_later_movies
    html = 'lab_10/movie/watch_later.html'
    return render(request, html, response)

### SESSION : GET and SET
def get_data_session(request):
    if request.session.get('user_login'):
        response['user_login'] = request.session.get('user_login')

def set_data_for_session(request):
    response['user_login'] = request.session.get('user_login')
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']


### API : SEARCH movie
def api_search_movie(request, judul, tahun):
    print ("API SEARCH MOVIE")
    if judul == "-" and tahun == "-":
        items = []
    else:
        search_results = search_movie(judul, tahun)
        items = search_results

    dataJson = json.dumps({"dataku":items})
    mimetype = 'application/json'
    return HttpResponse(dataJson, mimetype)