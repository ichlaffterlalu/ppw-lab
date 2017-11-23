# Lab 9 : Oauth, _Webservice_, beserta Pengenalan _Cookie_ dan _Session_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:
- Apa itu Cookie dan Session
- Memahami peran dan cara kerja Cookie & Session pada web
- Dapat menggunakan Cookie & Session 

## Hasil Akhir Lab
- Menggunakan session untuk :
    - Implementasi login dan logout
    - Membuat dan menghapus daftar favorit item
- Menggunakan cookies untuk :
    - Implementasi login dan logout
- Membuat halaman profile dan login (untuk metode Cookie dan Session)

## Self-Reflection
Sebelum mempelajari tutorial ini, mari kita mereview beberapa pengetahuan dasar:

- Apa itu HTTP? 
- Konsep-konsep dasar untuk HTTP
- Apa itu Cookie & Session penting?

## Pengenalan 

#### HTTP
HTTP merupakan singkatan dari _Hypertext Transfer Protocol_ adalah protokol yang digunakan
untuk berkomunikasi antara _clients_ dan _server_ . HTTP bersifat _stateless_, artinya antar _state_
atau aktifitas yang satu dengan yang lain bersifat independen (tidak terhubung). Setiap transaksi/aktifitas 
yang dilakukan dianggap sebagai transaksi/aktifitas yang benar-benar baru, tidak ada data sebelumnya 
yang disimpan untuk transkasi/aktifitas saat ini.

Contoh: kegiatan melempar dadu. Lemparan dadu yang pertama, kedua, ketiga dan seterusnya tidak
memiliki hubungan sama sekali. Setiap kegiatan melempar dadu, hasilnya tidak dipengaruhi oleh lemparan
dadu sebelum maupun sesudahnya. 
> Noted: _HTTP_ bersifat stateless. 

#### Pengetahuan dasar mengenai HTTP
Beberapa konsep atau pengetahuan dasar mengenai HTTP, antara lain : 
1. _Client/Server_: Interaksi dilakukan antar client/server. 
Client melakukan request dan server memberikan response
2. _Stateless_: Setiap aktifitas (request/response) bersifat independen
3. _Application Layer_ : Website berjalan pada _application layer_. Proses request/response terjadi
pada _Transport Layer_ yang umumnya menggunakan protokol TCP, yang menentukan bagaimana data akan dikirim,
_Application Layer_ tidak peduli apa yang dilakukan _Transport Layer_ (bagaimana data dikirim, diolah, dsb), _App layer_ hanya fokus pada request dan 
response.
4. _Client Actions Method_: Merupakan method yang digunakan oleh client saat melakukan request.
Contoh: GET, POST, PUT, DELETE, dll. 
5. _Server status code_: Merupakan status kode yang diberikan oleh server saat meminta suatu halaman web
Contoh: 200 (OK), 404 (Page not found), 500 (Internal Server Error), dsb.
6. _Headers_: Merupakan informasi kecil yang dikirim bersamaan dengan request dan response. 
Informasi-informasi tersebut berguna sebagai data tambahan yang digunakan untuk memproses request/response.
Contoh: Pada Headers terdapat content-type:json. Artinya tipe konten yang diminta/dikirim adalah json.
Headers juga menyimpan data _cookies_. 


#### Latar Belakang Cookies & Session
Semua komunikasi antara klien dan server dilakukan melalui protokol HTTP, dimana HTTP merupakan _stateless protocol_  
yang artinya state yang satu dengan yang lain tidak berhubungan (independen). Hal ini mengharuskan komputer klien yang
menjalankan _browser_ untuk membuat koneksi TCP ke server setiap kali melakukan request. 
Tanpa adanya koneksi persisten antara klien dan server, software pada setiap sisi (endpoint) tidak dapat bergantung 
hanya pada koneksi TCP untuk melakukan _holding state_ atau _holding session state_. 
Apa yang dimaksud dengan _holding state_?

Sebagai contoh, kamu ingin mengakses suatu halaman A pada suatu web yang mensyaratkan pengaksesnya sudah 
login ke dalam web.
Kemudian kamu login ke web tersebut dan berhasil membuka halaman A. Saat ingin pindah ke halaman B pada web yang sama, 
tanpa adanya suatu proses _holding state_ maka kamu akan diminta untuk login kembali. 
Begitu yang akan terjadi setiap kali kamu mengakses halaman yang berbeda padahal masih pada web yang sama.
Proses memberitahu 'siapa' yang sedang login dan menyimpan data ini dikenal sebagai bentuk dialog antara 
klien - server dan merupakan dasar session - _a semi-permanent exchange of information_. 
Merupakan hal yang sulit untuk membuat HTTP melakukan _holding state_ (karena HTTP merupakan stateless protocol). 
Oleh karena itu, dibutuhkan teknik untuk mengatasi masalah tersebut, yaitu Cookie dan Session. 

> Catatan: HTTP bersifat stateless. Bagaimana cara untuk membuat web (HTTP) menjadi stateful?

#### Cookies & Session
Salah satu cara yang paling banyak digunakan untuk melakukan _holding state_ adalah dengan menggunakan 
session ID yang disimpan sebagai cookie pada komputer klien. Session ID dapat dianggap sebagai suatu token 
(barisan karakter) untuk mengenali session yang unik pada aplikasi web tertentu. 
Daripada menyimpan semua jenis informasi sebagai cookies pada klien seperti username, nama dan password, 
hanya Session ID yang disimpan. Session ID ini kemudian dapat dipetakan ke suatu 
struktur data pada sisi web server. Pada struktur data tersebut, kamu dapat menyimpan semua informasi yang kamu butuhkan. 
Pendekatan ini jauh lebih aman untuk menyimpan informasi mengenai pengguna, daripada menyimpannya pada cookie.
Dengan cara ini, informasi tidak dapat disalah gunakan oleh klien atau koneksi yang mencurigakan. 
Selain itu, pendekatan ini lebih 'tepat' jika data yang akan disimpan ada banyak. Hal itu karena cookie hanya dapat 
menyimpan maksimal 4kb data. 
Bayangkan kamu sudah login ke suatu web / aplikasi dan mendapat session ID (session identifier). 
Untuk dapat melakukan _holding state_ pada HTTP yang _stateless_ , browser biasanya mengirimkan 
suatu session ID  ke server pada setiap _request_. Dengan begitu, setiap kali datang suatu _request_ , 
maka server akan bereaksi (kurang lebih) "Oh, Orang ini!" . Kemudian server akan mencari informasi _state_ di 
memori server atau di _database_  berdasarkan session ID yang didapat, dan mengembalikan data yang diminta.

Perbedaan penting yang perlu diingat, data Cookie disimpan pada sisi klien, 
sedangkan data Session biasanya disimpan pada sisi server.
Masih belum paham apa itu _stateless, stateful, cookies dan session_ ? 
Coba baca artikel berikut : 
[Stateless, Stateful, Coookies and Session](https://sethuramanmurali.wordpress.com/2013/07/07/stateful-stateless-cookie-and-session/)

Selanjutnya mengenai _storage_ atau penyimpanan data, 
kalian juga harus memahami perbedaan pada Cookies, Session Storage dan Local Storage. Coba perhatikan gambar dibawah ini, 
![alt text](http://tutorial.techaltum.com/images/Local-Storage-Vs-Session-Storage-Vs-Cookies.jpg)

> Berikut beberapa pranala video yang dapat membantu pemahaman terhadap Cookies dan Session: 
> [Session_Cookies](https://www.youtube.com/watch?v=64veb6tKTm0&t=10s), 
> [Cookies_history](https://www.youtube.com/watch?v=I01XMRo2ESg),
> [Perbedaan Cookies-Session-Local Storage](https://www.youtube.com/watch?v=AwicscsvGLg)

> Catatan : Cookies and Session make web (HTTP) stateful.


#### Informasi tambahan
1. Untuk dapat melihat data Cookies, gunakan browser Chrome tercinta, 
    - Tekan tombol F12 atau klik kanan -> Inspect element
    - Pilih tab `APPLICATION`,
    - Kemudian pada sidebar sebelah kiri, pilih menu `Cookies`, 
    - Pilih sub-menu yang merupakan web kalian (misalkan localhost:8000 jika mengerjakan di lokal)
    - Nanti akan muncul beberapa data, misalnya `csrftoken` lengkap dengan value, domain, masa kadaluarsa, dsb.


2. Mengapa menyimpan data (misalkan data user yang login) pada cookies tidak aman? 
   Apakah menyimpan data dengan session lebih aman? Bagaimana membuktikan hal ini? 
   
   >  Framework django memiliki 'key' cookies bernama `sessionid` yang menyimpan token unik setiap kali berhasil login 
   ke suatu web. Misalkan jalankan server pada localhost:8000, buka halaman A dan lakukan login. 
   Kemudian bukalah halaman lain (halaman B) menggunakan mode Incognito (penyamaran), buka web yang sama dan pastikan kamu belum login pada halaman B ini. 
   Salin `sessionid` (key-value) dari halaman A tempat kamu berhasil login, 
   kemudian isi cookie secara manual pada halaman B. Tekan F5. Tadaa! Analisa apa yang terjadi!
   
   > Catatan: Cookie dicek pada sisi klien, session dicek pada sisi server. 
   Jika suatu Session login sudah dihapus (logout), maka semua login yang menggunakan session yang sama otomatis 
   ikut ter-logout, karena pengecekan pada sisi server. Hal ini tidak berlaku untuk cookie.
   

## Membuat Halaman Aplikasi: Login, Profile, 
1. Jalankan virtual environment kalian
1. Buatlah _apps_ baru bernama `lab_9` , daftarkan di `INSTALLED_APPS`
1. Buatlah _Test Case_ baru kedalam `lab_9/tests.py`
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Tambahkan konfigurasi pada berkas `praktikum/urls.py` untuk app `lab_9` 
(Jika lupa caranya, cek ulang `lab_instruction` sebelumnya)
1. Buatlah konfigurasi URL di `lab_9/urls.py`:
    ```python
    from django.conf.urls import url
    from .views import index, profile, \
        add_session_drones, del_session_drones, clear_session_drones, \
        cookie_login, cookie_auth_login, cookie_profile, cookie_clear
    
    # sol to challenge
    from .views import add_session_item, del_session_item, clear_session_item
    # /sol
    from .custom_auth import auth_login, auth_logout
    
    urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^profile/$', profile, name='profile'),
    
        # custom auth
        url(r'^custom_auth/login/$', auth_login, name='auth_login'),
        url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),
    
        #add/delete drones
        url(r'^add_session_drones/(?P<id>\d+)/$', add_session_drones, name='add_session_drones'),
        url(r'^del_session_drones/(?P<id>\d+)/$', del_session_drones, name=''),
        url(r'^clear_session_drones/$', clear_session_drones, name='clear_session_drones'),
    
        # cookie
        url(r'^cookie/login/$', cookie_login, name='cookie_login'),
        url(r'^cookie/auth_login/$', cookie_auth_login, name='cookie_auth_login'),
        url(r'^cookie/profile/$', cookie_profile, name='cookie_profile'),
        url(r'^cookie/clear/$', cookie_clear, name='cookie_clear'), #sekaligus logout dari cookie
    
    ]
    ```
    > NOTE: Berikut 3 berkas bantuan (csui_helper.py, api_enterkomputer.py, custom_auth.py) yang satu level dengan views.py
    3 Berkas ini memiliki fungsi masing-masing. 
    
    > NOTE: GUNAKAN AKSES YANG DIBERIKAN DENGAN TANGGUNG JAWAB.
      POWER COMES WITH GREAT RESPONSIBILITY

1. Buat sebuah file bernama `csui_helper.py` : 
    ```python
    import requests
    
    API_MAHASISWA = "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/"
    API_VERIFY_USER = "https://akun.cs.ui.ac.id/oauth/token/verify/"
    def get_access_token(username, password):
        try:
            url = "https://akun.cs.ui.ac.id/oauth/token/"
    
            payload = "username=" + username + "&password=" + password + "&grant_type=password"
            headers = {
                'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
                'cache-control': "no-cache",
                'content-type': "application/x-www-form-urlencoded"
            }
            response = requests.request("POST", url, data=payload, headers=headers)
    
            return response.json()["access_token"]
        except Exception as e:
            return None
            # raise Exception("username atau password sso salah, input : [{}, {}]".format(username, password,))
    
    def get_client_id():
        client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
        return client_id
    
    def verify_user(access_token):
        print ("#get identity number")
        parameters = {"access_token": access_token, "client_id": get_client_id()}
        response = requests.get(API_VERIFY_USER, params=parameters)
        print ("response => ", response.json())
        return response.json()
    
    def get_data_user(access_token, id):
        print ("#get data user => ", id)
        parameters = {"access_token": access_token, "client_id": get_client_id()}
        response = requests.get(API_MAHASISWA+id, params=parameters)
        print ("response => ", response.text)
        print ("response => ", response.json())
        return response.json()
    ```
1. Buat berkas `api_enterkomputer.py` :
    ```python
    import requests
    
    DRONE_API       = 'https://www.enterkomputer.com/api/product/drone.json'
    SOUNDCARD_API   = 'https://www.enterkomputer.com/api/product/soundcard.json'
    OPTICAL_API     = 'https://www.enterkomputer.com/api/product/optical.json'
    
    def get_drones():
        drones = requests.get(DRONE_API)
        return drones
    
    # lengkapi pemanggilan utk SOUNDCARD_API dan OPTICAL_API untuk mengerjakan CHALLENGE
    
    ```
1. Buat berkas `custom_auth.py` :
    ```python
    from django.contrib import messages
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    
    from .csui_helper import get_access_token, verify_user
    
    #authentication
    def auth_login(request):
        print ("#==> auth_login ")
    
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
    
            #call csui_helper
            access_token = get_access_token(username, password)
            if access_token is not None:
                ver_user = verify_user(access_token)
                kode_identitas = ver_user['identity_number']
                role = ver_user['role']
    
                # set session
                request.session['user_login'] = username
                request.session['access_token'] = access_token
                request.session['kode_identitas'] = kode_identitas
                request.session['role'] = role
                messages.success(request, "Anda berhasil login")
            else:
                messages.error(request, "Username atau password salah")
        return HttpResponseRedirect(reverse('lab-9:index'))
    
    def auth_logout(request):
        print ("#==> auth logout")
        request.session.flush() # menghapus semua session
    
        messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
        return HttpResponseRedirect(reverse('lab-9:index'))
    ```
1. Masukkan kode berikut pada `views.py`
    ```python
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
    
    ```
1. Pada lab kali ini, tidak menggunakan model
1. Buatlah berkas `lab_9/templates/lab_9/layout/base.html`
    ```html
    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="description" content="LAB 9">
        <meta name="author" content="{{author}}">
    
        <!-- bootstrap csss -->
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .rata-tengah {
                text-align: center;
                margin : 20px;
            }
            .judul {
                text-transform:uppercase;
                margin-bottom: 50px;
                margin-top: 50px;
            }
        </style>
        <title>
            {% block title %} Lab 9 By {{author}} {% endblock %}
        </title>
    </head>
    <body>
    <header>
        <h1 style="text-align:center">
            <small><em> Change This With Your Custom Header </em></small>
        </h1>
        <!-- Your Header Here -->
    </header>
    <content>
        <div class="container">
            {% for message in messages %}
            <div class="alert {{ message.tags }} alert-dismissible" role="alert" id="django-messages">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close" style="margin-right: 15px;">
                    <span aria-hidden="true">&times;</span>
                </button>
                {{ message }}
            </div>
            {% endfor %}
    
            {% block content %}
            <!-- Your Content Here -->
            {% endblock %}
        </div>
    </content>
    <footer>
        <hr>
        {% block footer %}
    
        <h1 style="text-align:center">
            <small><em> Change This With Your Custom Footer </em></small>
        </h1>
        <!-- Your Footer Here -->
        {% endblock %}
    </footer>
    
    <!-- Jquery n Bootstrap Script -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
    </html>
    ```
    
    > Perhatikan bahwa tidak disediakan berkas CSS atau berkas Header dan Footer. 
    Kalian diminta untuk mendesain tampilan web kalian sehingga memiliki tampilan sebagus mungkin
    
Perhatikan bahwa kita akan menggunakan 2 metode: Session dan Cookies. 
Folder berkas html nya dipisahkan namun berkasnya memiliki nama yang sama, 
sehingga disarakan teliti dalam membuat struktur direktori agar tidak salah panggil.
      
#### Implementasi Session
1. Session Login: Buatlah berkas `lab_9/templates/lab_9/session/login.html` untuk simulasi login menggunakan _session_
    
    ```html
    {% extends "lab_9/layout/base.html" %}
    {% block content %}
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <div class="rata-tengah">
                <div class="judul">
                    <h1> Halaman Login </h1>
                    <p class="text-info"> Gunakan <b> akun SSO </b> untuk login </p>
                </div>
                <form action="{% url 'lab-9:auth_login' %}" method="POST">
                    {% csrf_token %}
                    <p>
                        <label for="username"> Your username </label>
                        <input type="text" id="username" name="username" required>
                    </p>
                    <p>
                        <label for="password"> Your password </label>
                        <input type="password" id="password" name="password" required>
                    </p>
                    <input type="submit" class="btn btn-primary">
                </form>
            </div>
        </div>
    </div>
    {% endblock %}
    ```
    
1. Session Profile: Buatlah berkas `lab_9/templates/lab_9/session/profile.html`
    ```html
    {% extends "lab_9/layout/base.html" %}
    {% block content %}
    <!-- Content Here -->
    <div class="pojok-kanan">
    </div>
    <br>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h2> [Session] Profile </h2>
        </div>
        <div class="panel-body">
            <p> Username : {{ author }} </p>
            <p> NPM : {{kode_identitas}} </p>
            <p> Role : {{ role }} </p>
        </div>
        <div class="panel-footer">
            <a href="{% url 'lab-9:auth_logout' %}" class="btn btn-danger pull-right" onclick="return confirm('Keluar?')">
                Logout </a>
            <a href="{% url 'lab-9:cookie_login' %}" class="btn btn-info"> Masuk Halaman Cookies </a>
        </div>
    </div>
    
    <div>
    
        <!-- Nav tabs -->
        <ul class="nav nav-tabs nav-justified" role="tablist">
            <li role="presentation" class="active">
                <a href="#drones" aria-controls="home" role="tab" data-toggle="tab"> Drones </a>
            </li>
            <li role="presentation">
                <a href="#soundcard" aria-controls="settings" role="tab" data-toggle="tab"> Soundcard </a>
            </li>
            <li role="presentation">
                <a href="#" aria-controls="settings" role="tab" data-toggle="tab"> Optical </a>
            </li>
        </ul>
    
        <!-- Tab panes -->
        <div class="tab-content">
            <div role="tabpanel" class="tab-pane fade in active" id="drones">
                {% include 'lab_9/tables/drones.html' %}
            </div>
            <div role="tabpanel" class="tab-pane fade" id="soundcard">
                <!-- Apply the same here -->
            </div>
            <div role="tabpanel" class="tab-pane fade" id="optical">
                <!-- Apply the same here -->
            </div>
        </div>
    </div>
    {% endblock %}
    ``` 
1. Berkas pendukung: buatlah berkas `lab_9/templates/lab_9/tables/drones.html`
    ```html
    <div class="panel panel-info">
        <div class="panel-heading">
            <h2> Daftar Drones : {{ drones | length}} </h2>
            <a href="{% url 'lab-9:clear_session_drones' %}" class="btn btn-danger" onclick="return confirm('Reset data?')">
                Reset Favorite Drones
            </a>
        </div>
        <div class="panel-body">
            <table class="table">
                <thead>
                <th> No</th>
                <th> Nama</th>
                <th> Harga</th>
                <th> Jumlah</th>
                <th> Aksi </th>
    
                </thead>
                <tbody>
                {% for drone in drones %}
                <tr>
                    <td> {{ forloop.counter }}</td>
                    <td> {{ drone.name }}</td>
                    <td> {{ drone.price }}</td>
                    <td> {{ drone.quantity }}</td>
                    <td>
                        {% if not drone.id in fav_drones %}
                        <a href="{% url 'lab-9:add_session_drones' drone.id %}" class="btn btn-primary"> Favoritkan </a>
                        {% else %}
                        <a href="{%url 'lab-9:del_session_drones' drone.id %}" class="btn btn-primary"> Hapus dari favorit </a>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    ```
#### Implementasi Cookie

1. Cookie Login: buatlah berkas `lab_9/templates/lab_9/cookie/login.html`
    ```html
    {% extends "lab_9/layout/base.html" %}
    {% block content %}
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
            <div class="rata-tengah">
                <div class="judul">
                    <h1> Login menggunakan COOKIES </h1>
                    <p class="text-danger"> Jangan menggunakan <b> akun SSO asli </b> </p>
                    <p class="text-danger"> karena Username dan password akan disimpan di dalam cookie </p>
                </div>
                <form action="{% url 'lab-9:cookie_auth_login' %}" method="POST">
                    {% csrf_token %}
                    <p>
                        <label for="username"> Your username* </label>
                        <input type="text" id="username" name="username" required>
                    </p>
                    <p>
                        <label for="password"> Your password* </label>
                        <input type="password" id="password" name="password" required>
                    </p>
                    <input type="submit" class="btn btn-primary">
                </form>
            </div>
        </div>
    </div>
    {% endblock %}
    ```
2. Cookie Profile: buatlah berkas `lab_9/templates/lab_9/cookie/profile.html`:
    ```html
    {% extends "lab_9/layout/base.html" %}
    
    {% block content %}
    <br>
    <div class="panel panel-default">
        <div class="panel-heading">
            <h2> [Cookie] Profile </h2>
        </div>
        <div class="panel-body">
            <p> Username : {{ request.COOKIES.user_login }} </p>
        </div>
        <div class="panel-footer">
            <a href="{% url 'lab-9:cookie_clear' %}" class="btn btn-danger"> Reset Cookies (Logout) </a>
        </div>
    </div>
    {% endblock %}
    ```

#### Challenge
Untuk membantu kalian dalam mengerjakan challenge, telah disiapkan beberapa baris kode untuk membantu

1. Implementasi tambah/hapus item dari session secara umum:
    ```python
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
    ```
1. Dilengkapi dengan urls.py:
    ```python
    #general function : solution to challenge
        url(r'^add_session_item/(?P<key>\w+)/(?P<id>\d+)/$', add_session_item, name='add_session_item'),
        url(r'^del_session_item/(?P<key>\w+)/(?P<id>\d+)/$', del_session_item, name='del_session_item'),
        url(r'^clear_session_item/(?P<key>\w+)/$', clear_session_item, name='clear_session_item'),
    ```
## Checklist
### Mandatory 

1. Session: Login & Logout
    1. [ ] Implementasi fungsi Login 
    2. [ ] Implementasi fungsi Logout 
    
2. Session: Kelola Favorit
    1. [ ] Implementasi fungsi "Favoritkan" untuk Drones
    2. [ ] Implementasi fungsi "Hapus dari favorit" untuk Drones
    2. [ ] Implementasi fungsi "Reset favorit" untuk Drones

3. Cookies: Login & Logout
    1. [ ] Implementasi fungsi Login
    2. [ ] Implementasi fungsi Logout

4. Implementasi Header dan Footer
    1. [ ] Buatlah header yang berisi tombol Logout *hanya jika* sudah login 
    (baik pada session dan cookies). Buatlah sebagus dan semenarik mungkin.
    
3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%

### Challenge
1. Implementasi API Optical dan SoundCard
    1. [ ] Menambahkan link ke tab Optical dan Soundcard pada halaman Session Profile
    1. [ ] Membuat tabel berisi data optical/soundcard 
    
2. Implementasi fungsi umum yang sudah disediakan mengelola session:
    1. [ ] Menggunakan fungsi umum untuk menambahkan (Favoritkan) optical/soundcard ke session
    2. [ ] Menggunakan fungsi umum untuk menghapus (Hapus dari Favorit) optical/soundcard dari session
    3. [ ] Menggunakan fungsi umum untuk menghapus/reset kategori (drones/optical/soundcard) dari session.

3. Implementasi _session_ untuk semua halaman yang telah dibuat pada Lab Sebelumnya
    1. [ ] Jika halaman lab diakses tanpa login terlebih dahulu, maka mereka akan ditampilkan halaman login
    2. [ ] Ketika halaman Lab ke-**N** diakses tanpa login, maka setelah login, pengguna akan diberikan tampilan Lab ke-**N**
    3. [ ] Ubahlah implementasi `csui_helper.py` pada Lab 9 sehingga bisa digunakan oleh Lab 7 (Kalian boleh menghapus berkas `csui_helper.py`
    yang ada di Lab 7)
      
