# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'
from .api_enterkomputer import get_drones, get_soundcards, get_opticals
from lab_login.custom_auth import check_login

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? melakukan cek apakah login atau tidak, lalu
# apabila sudah login, akan dialihkan ke profile page
def index(request):
    html = HttpResponseRedirect(reverse('lab-9:profile'))
    html = check_login(request, html, response)

    if type(html) == HttpResponseRedirect: return html
    else: return render(request, html, response)

def set_data_for_session(response, request):
    response['user_login'] = request.session['user_login']
    response['access_token'] = request.session['access_token']
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']
    response['drones'] = get_drones().json()
    response['soundcards'] = get_soundcards().json()
    response['opticals'] = get_opticals().json()

    ## handling agar tidak error saat pertama kali login (session kosong)
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    if 'drones' in request.session.keys():
        response['fav_drones'] = request.session['drones']
    else:
        response['fav_drones'] = []

    if 'soundcards' in request.session.keys():
        response['fav_soundcards'] = request.session['soundcards']
    else:
        response['fav_soundcards'] = []

    if 'opticals' in request.session.keys():
        response['fav_opticals'] = request.session['opticals']
    else:
        response['fav_opticals'] = []

def profile(request):
    html = 'lab_9/session/profile.html'
    html_after = check_login(request, html, response)
    if html != html_after: return render(request, html_after, response)

    set_data_for_session(response, request)
    return render(request, html, response)

# ======================================================================== #
# COOKIES

# Apa yang dilakukan fungsi INI? Merupakan mekanisme login menggunakan cookie
def cookie_login(request):
    if is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_profile'))
    else:
        html = 'lab_9/cookie/login.html'
        return render(request, html, response)

def cookie_auth_login(request):
    if request.method == "POST":
        user_login = request.POST['username']
        user_password = request.POST['password']

        if my_cookie_auth(user_login, user_password):
            res = HttpResponseRedirect(reverse('lab-9:cookie_login'))

            res.set_cookie('user_login', user_login)
            res.set_cookie('user_password', user_password)

            return res
        else:
            msg = "Username atau Password Salah"
            messages.error(request, msg)
            return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))

def cookie_profile(request):
    # method ini untuk mencegah error ketika akses URL secara langsung
    if not is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        in_uname = request.COOKIES['user_login']
        in_pwd= request.COOKIES['user_password']

        # jika cookie diset secara manual (usaha hacking), distop dengan cara berikut
        # agar bisa masuk kembali, maka hapus secara manual cookies yang sudah diset
        if my_cookie_auth(in_uname, in_pwd):
            html = "lab_9/cookie/profile.html"
            res =  render(request, html, response)
            return res
        else:
            msg = "Kamu tidak punya akses :P "
            messages.error(request, msg)
            html = "lab_9/cookie/login.html"
            return render(request, html, response)

def cookie_clear(request):
    res = HttpResponseRedirect('/lab-9/cookie/login')
    res.delete_cookie('lang')
    res.delete_cookie('user_login')

    msg = "Anda berhasil logout. Cookies direset"
    messages.info(request, msg)
    return res

# Apa yang dilakukan fungsi ini?
def my_cookie_auth(in_uname, in_pwd):
    my_uname = "utest" #SILAHKAN ganti dengan USERNAME yang kalian inginkan
    my_pwd = "ptest" #SILAHKAN ganti dengan PASSWORD yang kalian inginkan
    return in_uname == my_uname and in_pwd == my_pwd

#Apa yang dilakukan fungsi ini?
def is_login(request):
    return 'user_login' in request.COOKIES and 'user_password' in request.COOKIES

# ======================================================================== #
# SESSION ITEM FUNCTIONS (GENERAL)

def add_session_item(request, key, id):
    dummy_response = check_login(request, False, response)
    if dummy_response: return render(request, dummy_response, response)
    else:
        ssn_key = request.session.keys()
        if not key in ssn_key:
            request.session[key] = [id]
        else:
            items = request.session[key]
            if id not in items:
                items.append(id)
                request.session[key] = items

        messages.success(request, "Berhasil tambah " + key + "favorite")
        return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_item(request, key, id):
    items = request.session[key]
    items.remove(id) #untuk remove id tertentu dari list
    request.session[key] = items

    messages.error(request, "Berhasil hapus item " + key + " dari favorite")
    http_response = HttpResponseRedirect(reverse('lab-9:profile'))
    http_response = check_login(request, http_response, response)
    if type(http_response) == str: return (request, http_response, response)
    else: return http_response

def clear_session_item(request, key):
    dummy_response = check_login(request, False, response)
    if dummy_response: return render(request, dummy_response, response)
    else:
        ssn_key = request.session.keys()
        if key in ssn_key:
            del request.session[key]
            messages.error(request, "Berhasil hapus session: favorite " + key)
            return HttpResponseRedirect(reverse('lab-9:index'))
        else:
            messages.error(request, "Favorite " + key + " kosong")
            return HttpResponseRedirect(reverse('lab-9:index'))

# ======================================================================== #