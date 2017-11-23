# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
#catatan: tidak bisa menampilkan messages jika bukan menggunakan method 'render'
from .api_enterkomputer import get_drones

response = {}

# NOTE : untuk membantu dalam memahami tujuan dari suatu fungsi (def)
# Silahkan jelaskan menggunakan bahasa kalian masing-masing, di bagian atas
# sebelum fungsi tersebut.

# ======================================================================== #
# User Func
# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian
def index(request):
    print ("#==> masuk index")
    if 'user_login' in request.session:
        return HttpResponseRedirect(reverse('lab-9:profile'))
    else:
        html = 'lab_9/session/login.html'
        return render(request, html, response)

def set_data_for_session(res, request):
    response['author'] = request.session['user_login']
    response['access_token'] = request.session['access_token']
    response['kode_identitas'] = request.session['kode_identitas']
    response['role'] = request.session['role']
    response['drones'] = get_drones().json()

    # print ("#drones = ", get_drones().json(), " - response = ", response['drones'])
    ## handling agar tidak error saat pertama kali login (session kosong)
    if 'drones' in request.session.keys():
        response['fav_drones'] = request.session['drones']
    # jika tidak ditambahkan else, cache akan tetap menyimpan data
    # sebelumnya yang ada pada response, sehingga data tidak up-to-date
    else:
        response['fav_drones'] = []

def profile(request):
    print ("#==> profile")
    ## sol : bagaimana cara mencegah error, jika url profile langsung diakses
    if 'user_login' not in request.session.keys():
        return HttpResponseRedirect(reverse('lab-9:index'))
    ## end of sol

    set_data_for_session(response, request)

    html = 'lab_9/session/profile.html'
    return render(request, html, response)

# ======================================================================== #

### Drones
def add_session_drones(request, id):
    ssn_key = request.session.keys()
    if not 'drones' in ssn_key:
        print ("# init drones ")
        request.session['drones'] = [id]
    else:
        drones = request.session['drones']
        print ("# existing drones => ", drones)
        if id not in drones:
            print ('# add new item, then save to session')
            drones.append(id)
            request.session['drones'] = drones

    messages.success(request, "Berhasil tambah drone favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_drones(request, id):
    print ("# DEL drones")
    drones = request.session['drones']
    print ("before = ", drones)
    drones.remove(id) #untuk remove id tertentu dari list
    request.session['drones'] = drones
    print ("after = ", drones)

    messages.error(request, "Berhasil hapus dari favorite")
    return HttpResponseRedirect(reverse('lab-9:profile'))

def clear_session_drones(request):
    print ("# CLEAR session drones")
    print ("before 1 = ", request.session['drones'])
    del request.session['drones']

    messages.error(request, "Berhasil reset favorite drones")
    return HttpResponseRedirect(reverse('lab-9:profile'))

# ======================================================================== #
# COOKIES

# Apa yang dilakukan fungsi INI? #silahkan ganti ini dengan penjelasan kalian
def cookie_login(request):
    print ("#==> masuk login")
    if is_login(request):
        return HttpResponseRedirect(reverse('lab-9:cookie_profile'))
    else:
        html = 'lab_9/cookie/login.html'
        return render(request, html, response)

def cookie_auth_login(request):
    print ("# Auth login")
    if request.method == "POST":
        user_login = request.POST['username']
        user_password = request.POST['password']

        if my_cookie_auth(user_login, user_password):
            print ("#SET cookies")
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
    print ("# cookie profile ")
    # method ini untuk mencegah error ketika akses URL secara langsung
    if not is_login(request):
        print ("belum login")
        return HttpResponseRedirect(reverse('lab-9:cookie_login'))
    else:
        # print ("cookies => ", request.COOKIES)
        in_uname = request.COOKIES['user_login']
        in_pwd= request.COOKIES['user_password']

        # jika cookie diset secara manual (usaha hacking), distop dengan cara berikut
        # agar bisa masuk kembali, maka hapus secara manual cookies yang sudah diset
        if my_cookie_auth(in_uname, in_pwd):
            html = "lab_9/cookie/profile.html"
            res =  render(request, html, response)
            return res
        else:
            print ("#login dulu")
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


### General Function
def add_session_item(request, key, id):
    print ("#ADD session item")
    ssn_key = request.session.keys()
    if not key in ssn_key:
        request.session[key] = [id]
    else:
        items = request.session[key]
        if id not in items:
            items.append(id)
            request.session[key] = items

    msg = "Berhasil tambah " + key +" favorite"
    messages.success(request, msg)
    return HttpResponseRedirect(reverse('lab-9:profile'))

def del_session_item(request, key, id):
    print ("# DEL session item")
    items = request.session[key]
    print ("before = ", items)
    items.remove(id)
    request.session[key] = items
    print ("after = ", items)

    msg = "Berhasil hapus item " + key + " dari favorite"
    messages.error(request, msg)
    return HttpResponseRedirect(reverse('lab-9:profile'))

def clear_session_item(request, key):
    del request.session[key]
    msg = "Berhasil hapus session : favorite " + key
    messages.error(request, msg)
    return HttpResponseRedirect(reverse('lab-9:index'))

# ======================================================================== #