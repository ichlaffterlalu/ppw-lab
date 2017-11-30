# Lab 10 : Penerapan Lanjut _Cookie_ dan _Session_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:
- Cara menggunakan OMDb API (The Open Movie Database)
- Cara menggunakan plug-in DataTables
- Cara menggunakan session dan model untuk menyimpan data

## Hasil Akhir Lab
- Menggunakan fitur Login
- Menampilkan list film dari OMDb API
- Membuat fungsi pencarian film
- Menambahkan fitur "Watch Later" menggunakan session dan model


## Self-Reflection
Untuk dapat mengerjakan tutorial ini, kamu harus mengingat dan mengerti : 

1. Cara mengakses dan mengelola data sesuai dengan tipe data-nya (`dict, list, json`, dsb)

1. Cara menggunakan session (menambah dan menghapus item dari session)

1. Cara menggunakan Django Model (menambah dan menghapus item)


## Informasi Tambahan
#### OMDB API
Tutorial Lab 10 menggunakan [OMDb API](http://www.omdbapi.com/) untuk  mendapatkan daftar film. 
Untuk dapat menggunakan API ini, terlebih dahulu kamu harus mendapatkan [API KEY](http://www.omdbapi.com/apikey.aspx)
Pelajari bagaimana cara mendapatkan dan menggunakannya. 

#### DataTables
Datatables adalah salah satu _plugin_ JQuery yang _powerful_. Pada tutorial kali ini, kalian akan belajar
**salah satu cara ** menggunakan DataTables yaitu dengan Ajax dan 
[custom data property](https://datatables.net/examples/ajax/custom_data_property.html). 


## Peringatan
Pada lab ini kalian diharappkan untuk lebih banyak berkreasi. Lab ini hanya menyediakan _template_
dan instruksi sederhana. Penamaan berkas HTML atau Python beserta penempatannya didalam struktur _project_
silahkan kalian ubah sesuai dengan keinginan kalian. Kami menganggap bahwa kalian sudah cukup baik dalam
membuat sebuah _web_ yang baik dengan kreasi kalian sendiri.

## Membuat Halaman Aplikasi: Login & Dashboard
1. Lakukan langkah-langkah konfigurasi untuk pembuatan Lab 10 (sama seperti Lab-Lab sebelumnya)

1. Buatlah konfigurasi URL di `lab_10/urls.py`:
    ```python
    from django.conf.urls import url
    from .views import *
    
    from .custom_auth import auth_login, auth_logout
    
    urlpatterns = [
        # custom auth
        url(r'^custom_auth/login/$', auth_login, name='auth_login'),
        url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),
    
        # index dan dashboard
        url(r'^$', index, name='index'),
        url(r'^dashboard/$', dashboard, name='dashboard'),
    
        #movie
        url(r'^movie/list/$', movie_list, name='movie_list'),
        url(r'^movie/detail/(?P<id>.*)/$', movie_detail, name='movie_detail'),
    
        # Session dan Model (Watch Later)
        url(r'^movie/watch_later/add/(?P<id>.*)/$', add_watch_later, name='add_watch_later'),
        url(r'^movie/watch_later/$', list_watch_later, name='list_watch_later'),
    
        #API
        url(r'^api/movie/(?P<judul>.*)/(?P<tahun>.*)/$', api_search_movie, name='api_search_movie'),
    ]
    ```
1. Gunakan berkas `csui_helper.py` pada Lab 9 untuk fungsi Login

1. Gunakan berkas `custom_auth.py` pada Lab 9 untuk fungsi autentikasi
> Catatan : Silahkan lakukan perubahan kode sesuai dengan kebutuhan kalian

1. Masukkan kode berikut pada `views.py`

    ```python
    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals
    
    import json
    
    from django.contrib import messages
    from django.http import HttpResponseRedirect, HttpResponse
    from django.shortcuts import render
    from django.urls import reverse
    
    from .omdb_api import get_detail_movie, search_movie
    from .utils import *
    response = {}
    
    # Create your views here.
    
    ### USER
    def index(request):
        # print ("#==> masuk index")
        if 'user_login' in request.session:
            return HttpResponseRedirect(reverse('lab-10:dashboard'))
        else:
            response['author'] = get_data_user(request, 'user_login')
            html = 'lab_10/login.html'
            return render(request, html, response)
    
    def dashboard(request):
        print ("#==> dashboard")
    
        if not 'user_login' in request.session.keys():
            return HttpResponseRedirect(reverse('lab-10:index'))
        else:
            set_data_for_session(request)
            kode_identitas = get_data_user(request, 'kode_identitas')
            try:
                pengguna = Pengguna.objects.get(kode_identitas = kode_identitas)
            except Exception as e:
                pengguna = create_new_user(request)
    
            movies_id = get_my_movies_from_session(request)
            save_movies_to_database(pengguna, movies_id)
    
            html = 'lab_10/dashboard.html'
            return render(request, html, response)
    
    
    ### MOVIE : LIST and DETAIL
    def movie_list(request):
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
        if get_data_user(request, 'user_login'):
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
        if get_data_user(request, 'user_login'):
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
    
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('lab-10:movie_detail', args=(id,)))
    
    def list_watch_later(request):
        #  Implement this function by yourself
        get_data_session(request)
        moviesku = []
        if get_data_user(request, 'user_login'):
            moviesku = get_my_movies_from_database(request)
        else:
            moviesku = get_my_movies_from_session(request)
    
        watch_later_movies = get_list_movie_from_api(moviesku)
    
        response['watch_later_movies'] = watch_later_movies
        html = 'lab_10/movie/watch_later.html'
        return render(request, html, response)
    
    ### SESSION : GET and SET
    def get_data_session(request):
        if get_data_user(request, 'user_login'):
            response['author'] = get_data_user(request, 'user_login')
    
    def set_data_for_session(request):
        response['author'] = get_data_user(request, 'user_login')
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

    ```

1. Masukkan kode berikut kedalam `models.py`
    ```python
    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals
    
    from django.db import models
    
    # Create your models here.
    class Pengguna(models.Model):
        kode_identitas = models.CharField('Kode Identitas', max_length=20, primary_key=True, )
        nama = models.CharField('Nama', max_length=200)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
    class MovieKu(models.Model):
        pengguna = models.ForeignKey(Pengguna)
        kode_movie = models.CharField("Kode Movie", max_length=50)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```
1. Buatlah berkas `omdb_api.py` di dalam `lab_10`
    ```python
    import requests
    API_KEY = "" #TODO Implement, fill your OMDB API Key Here
    
    def search_movie(judul, tahun):
        print ("METHOD SEARCH MOVIE")
        get_tahun = ""
        if not tahun == "-":
            get_tahun = "&y="+tahun
        url = "http://www.omdbapi.com/?s=" + judul + get_tahun + "&apikey=" + API_KEY ;
        req = requests.get(url)
        resp = req.json()
    
        data_exist = False
        stResponse = resp['Response']
        print ("RESPONSE => ", stResponse)
        if stResponse == "True":
            count_results = resp['totalResults']
    
            #cukup ambil 30 data saja
            cp = (int(count_results) / 10)
            if cp > 3: pages = 3
            elif cp > 0 and cp <= 3: pages = cp
            else: pages = 1
            data_exist = True
    
        past_url = url
        all_data = []
        if data_exist:
            for page in range(pages):
                page += 1
                get_page = "&page="+str(page)
                new_url = past_url + get_page;
                new_req = requests.get(new_url).json()
                get_datas = new_req['Search']
                for data in get_datas:
                    all_data.append(data)
    
        return all_data
    
    
    def get_detail_movie(id):
        url = "http://www.omdbapi.com/?i="+id+"&apikey="+API_KEY;
        req = requests.get(url)
        rj = req.json() # dict
        my_list = create_json_from_dict(rj)
    
        return my_list
    
    def create_json_from_dict(your_dict):
        your_data = {}
        for key in your_dict:
            cvalue = (your_dict.get(key))
            nk = str(key).lower()
            if type(cvalue) == list:
                nv = cvalue
            else:
                nv = cvalue.encode('ascii','ignore')
            your_data[nk] = nv
        return your_data
    ```
1. Buatlah `utils.py` di dalam `lab_10`
    ```python
    
    from .models import Pengguna, MovieKu
    from .omdb_api import get_detail_movie
    
    def check_movie_in_database(request, kode_movie):
        is_exist = False
        kode_identitas = get_data_user(request, 'kode_identitas')
        pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
        count_movie = MovieKu.objects.filter(pengguna=pengguna, kode_movie=kode_movie).count()
        if count_movie > 0 :
            is_exist = True
    
        return is_exist
    
    def check_movie_in_session(request, kode_movie):
        is_exist = False
        ssn_key = request.session.keys()
        if 'movies' in ssn_key:
            movies = request.session['movies']
            if kode_movie in movies:
                is_exist = True
    
        return is_exist
    
    def add_item_to_database(request, id):
        kode_identitas = get_data_user(request, 'kode_identitas')
        pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
        movieku = MovieKu()
        movieku.kode_movie = id
        movieku.pengguna = pengguna
        movieku.save()
    
    def add_item_to_session(request, id):
        ssn_key = request.session.keys()
        if not 'movies' in ssn_key:
            request.session['movies'] = [id]
        else:
            movies = request.session['movies']
            # check apakah di session sudah ada key yang sama
            if id not in movies:
                movies.append(id)
                request.session['movies'] = movies
    
    
    def get_data_user(request, tipe):
        data = None
        if tipe == "user_login" and 'user_login' in request.session:
            data = request.session['user_login']
        elif tipe == "kode_identitas" and 'kode_identitas' in request.session:
            data = request.session['kode_identitas']
    
        return data
    
    def create_new_user(request):
        nama = get_data_user(request, 'user_login')
        kode_identitas = get_data_user(request, 'kode_identitas')
    
        pengguna = Pengguna()
        pengguna.kode_identitas = kode_identitas
        pengguna.nama = nama
        pengguna.save()
    
        return pengguna
    
    def get_parameter_request(request):
        if request.GET.get("judul"):
            judul = request.GET.get("judul")
        else:
            judul = "-"
    
        if request.GET.get("tahun"):
            tahun = request.GET.get("tahun")
        else:
            tahun = "-"
    
        return judul, tahun
    
    # after login, save movies from session
    def save_movies_to_database(pengguna, list_movie_id):
        #looping get id, cek apakah exist berdasarkan user, jika tidak ada, maka tambah
    
        for movie_id in list_movie_id:
            if not (MovieKu.objects.filter(pengguna = pengguna, kode_movie = movie_id).count()) > 0:
                new_movie = MovieKu()
                new_movie.pengguna = pengguna
                new_movie.kode_movie = movie_id
                new_movie.save()
    
    #return movies user from db
    def get_my_movies_from_database(request):
        resp = []
        kode_identitas = get_data_user(request, 'kode_identitas')
        pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
        items = MovieKu.objects.filter(pengguna=pengguna)
        for item in items:
            resp.append(item.kode_movie)
        return resp
    
    #get my movies from session
    def get_my_movies_from_session(request):
        resp = []
        ssn_key = request.session.keys()
        if 'movies' in ssn_key:
            resp = request.session['movies']
        return resp
    
    #get detail list movie from api
    def get_list_movie_from_api(my_list):
        print ("GET LIST DATA")
        list_movie = []
        for movie in my_list:
            list_movie.append(get_detail_movie(movie))
    
        return list_movie

    ```
1. Buatlah berkas `base.html` (dapat menggunakan `base.html` yang 
    sudah kalian buat pada Lab 9 beserta _header_ dan _footer_ nya)
1. Buatlah halaman untuk Login 
1. Buatlah halaman untuk Dashboard
    ```html
    {% extends "lab_10/layout/base.html" %}
    
    {% block content %}
    <!-- Content Here -->
    <section id="data-dashboard">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h2> Dashboard </h2>
            </div>
            <div class="panel-body">
                <p> Username : {{ author }} </p>
                <p> NPM : {{kode_identitas}} </p>
                <p> Role : {{ role }} </p>
                <p>
                    <a href="{% url 'lab-10:movie_list' %}" class="btn btn-primary"> Daftar Movie </a> |
                    <a href="{% url 'lab-10:list_watch_later' %}" class="btn btn-warning"> Daftar Watch Later </a>
                </p>
            </div>
            <div class="panel-footer">
                <a href="{% url 'lab-10:auth_logout' %}" class="btn btn-danger" onclick="return confirm('Keluar?')">
                    Logout </a>
            </div>
        </div>
    </section>
    <hr>
    
    {% endblock %}
    ```
1. Buatlah halaman `detail.html`
    ```html
    {% extends "lab_10/layout/base.html" %}
    
    {% block content %}
    <div class="row">
        <h1> Catatan : Buatlah halaman detail movie sesuai selera dan kreatifitas kalian </h1>
    
        <br>
        <h2> Raw Data (json) </h2>
        <p> {{ movie }} </p>
        <hr>
        <h2> Contoh cara mengambil judul: </h2>
        <h1 style="color:red"> {{ movie.title}} </h1>
    
        <br>
        <div class="box">
            {% if added %}
            <button class="btn btn-success"> Added to Watch Later </button>
            {% else %}
            <a href="{% url 'lab-10:add_watch_later' id %}" class="btn btn-warning"> Add to Watch Later </a>
            {% endif%}
        </div>
    
    
    </div>
    {% endblock %}
    ```
1. Buatlah halaman `list.html`
    ```html
    {% extends "lab_10/layout/base.html" %}

    {% block content %}
    <!-- User Login Here -->
    {% if user_login %}
    <a href="" class="btn btn-primary btn-lg"> Logout </a>
    
    {% else %}
    <p>
        <a href="{% url 'lab-10:list_watch_later' %}" class="btn btn-primary btn-lg "> Daftar <em>Watch Later </em> </a>
    </p>
    
    {% endif %}
    <br>
    <!-- List Movie -->
    <div class="panel panel-info">
        <div class="panel-heading">
            <h2> List Movie </h2>
        </div>
        <div class="panel-body">
            <div style="margin:20px; padding:20px; background-color:lightsteelblue; border-radius:3px;">
                <form method="GET" action="{% url 'lab-10:movie_list' %}" class="form-inline">
                    <label> Nama </label> <input type="text" class="form-control" name="judul" placeholder="Judul"
                                                 value="{{judul}}">
                    <label> Tahun </label> <input type="text" class="form-control" name="tahun" placeholder="Tahun "
                                                  value="{{tahun}}">
                    <input type="submit" class="btn btn-primary pull-right">
                </form>
            </div>
            <hr>
            <div class="table table-responsive">
                <table class="table table-hover" id="myTable" style="width: none;">
                    <thead>
                    <th> Judul</th>
                    <th> Tahun</th>
                    <th> Poster</th>
                    <th> Detail</th>
                    </thead>
                </table>
            </div>
        </div>
    </div>
    
    <!-- Jquery script -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(e) {
            $('#myTable').DataTable( {
                "ajax": {
                    "dataType" : 'json',
                    "contentType": "application/json; charset=utf-8",
                    "url": {% autoescape off %} {{ jsonUrlDT }} {% endautoescape%} ,
                    "dataSrc":"dataku",
                },
                "columns" : [
                    {"data" : "Title"},
                    {"data" : "Year"},
                    {
                        "data" : "Poster",
                        "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                            $(nTd).html("<img src='"+ oData.Poster +"' style='height:50%' class='img-responsive img-thumbnail'/>");
                        }
                    },
                    {
                        "data" : null,
                        "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
                            $(nTd).html("<a href='/lab-10/movie/detail/"+ oData.imdbID +"' class='btn btn-primary'> Detail </a>");
                        }
                    }
                ],
            } );
        });
    </script>
    
    
    {% endblock %}

    ```
1. Buatlah halaman `watch_later.html`
    ```html
    {% extends "lab_10/layout/base.html" %}

    {% block content %}
    <div class="row">
        {% for movie in watch_later_movies %}
        <p> {{ movie }} </p>
        {% endfor %}
    </div>
    {% endblock %}
    ``` 

## Checklist
### Mandatory 

1. Autentikasi :
    1. [ ] Implementasi fungsi Login & Logout
    1. [ ] Melakukan pengecekan setiap mengakses suatu halaman, apakah sudah login 
    apa belum (jika belum login, arahkan ke halaman login)
    1. [ ] (Jelaskan) Bagaimana Django Apps kalian mengetahui bahwa setiap _user_ yang menagkses Apps kalian,
    akan dilayani secara berbeda? (Data milik pengguna tidak akan saling tertukar). Tunjukkan didalam baris kode
    
1. Dashboard : 
    1. [ ] Mendaftar dan menggunakan OMDb API untuk menampilkan daftar film
    1. [ ] Menggunakan DataTables untuk menampilkan daftar film dan filtering
    1. [ ] Membuat fungsi pencarian film berdasarkan judul dan tahun
    1. [ ] (Jelaskan) Bagaimana Django Apps kalian bisa melakukan _pagination_ dan melakukan pencarian?

1. Koleksi Film
    1. [ ] Membuat daftar film "tonton nanti" (disimpan di session)
    1. [ ] Membuat daftar film "sudah ditonton" (disimpan di model)
    1. [ ] (Jelaskan) Bagaimana Django Apps kalian bisa menyimpan film yang ingin ditonton, tanpa Login terlebih dahulu?
    1. [ ] (Jelaskan) Bagaimana Django Apps kalian bisa menyimpan film yang ingin ditonton kedalam _database_, dan membedakan
    kepemilikan dari massing - masing daftar film? Tunjukkan dalam baris kode

1. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%

#### Challenge
1. Membuat halaman untuk fitur List My Watch Later
1. Membuat penanganan jika suatu movie ditambahkan secara manual 
    