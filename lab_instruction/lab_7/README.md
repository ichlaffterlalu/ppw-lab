# Lab 7 : Pengenalan _Web Service_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:
- Apa itu Webservice, ajax dan json
- Mampu menggunakan webservice, ajax, dan json

## Hasil Akhir Lab
- Membuat halaman berisi daftar mahasiswa fasilkom ui menggunakan api dari api-dev.cs.ui.ac.id

## Self-Reflection
Sebelum mempelajari tutorial ini, mari kita mereview beberapa pengetahuan dasar yang sudah pernah kita bahas dan pelajari sebelumnya.

- Apakah kamu tahu cara web bekerja? Apa yang dilakukan browsermu saat membuka suatu link? Apa itu HTTP? Requests dan response? Jika tidak, maka kamu perlu baca dan pelajari kembali!
- Apa itu Django? Model, Views, Template?
- HTML, CSS, dan DOM? Apa kegunaan javascript? Dan bagaimana cara menjalankan suatu script javascript pada suatu page?

## Pengenalan

#### API
Sebelum memahami web service, ada baiknya kita mengetahui apa itu API. Pada saat kita melakukan koding dengan bahasa pemrograman java, kita mungkin sudah pernah berkenalan dengan API. API merupakan suatu interface yang dalam hal ini berupa sekumpulan fungsi/method yang digunakan suatu program untuk berkomunikasi/menjalankan/menggunakan program lain tanpa perlu mengetahui kompleksitas dari fungsi tersebut. Java menyediakan banyak sekali api (lihat https://docs.oracle.com/javase/7/docs/api/) contohnya ketika kita ingin membuat GUI pada program java kita, kita dapat menggunakan swing api dengan melakukan import dan menggunakan fungsi-fungsi yang disediakan, kemudian kita dapat menampilkan sebuah panel yang terdapat text field atau button di dalamnya dengan menggunakan fungsi-fungsi tersebut tanpa mengetahui kompleksitas di dalamnya.

#### Apa itu Web Service
Lalu apa itu web service? Web service merupakan API yang dibungkus dalam HTTP yang membuat dua mesin berbeda dapat berkomunikasi. Jika API merupakan interface untuk komunikasi antar program, web service digunakan untuk berkomunikasi antar mesin (dikenal juga dengan istilah Web Based API) melalui network.

#### Apa itu Json
JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan, mudah dibaca dan ditulis oleh manusia, serta mudah diterjemahkan dan dibuat (generate) oleh komputer. Format ini dibuat berdasarkan bagian dari Bahasa Pemprograman JavaScript, Stkitar ECMA-262 Edisi ke-3 - Desember 1999. JSON merupakan format teks yang tidak bergantung pada bahasa pemprograman apapun karena menggunakan gaya bahasa yang umum digunakan oleh programmer keluarga C termasuk C, C++, C#, Java, JavaScript, Perl, Python dll. Oleh karena sifat-sifat tersebut, menjadikan JSON ideal sebagai bahasa pertukaran-data.

Berikut ini merupakan contoh format json

```
{
    “Nama”: “kak pewe”,
    “Age”: 2017,
    “Message”: [“semoga soalnya susah”, ”yang buat aufa”] //list message
}
```

untuk lebih lengkapnya bisa lihat di http://www.json.org/json-id.html

#### Apa itu AJAX

Asynchronous JavaScript and XMLHTTP, atau disingkat AJaX, adalah suatu teknik pemrograman berbasis web untuk menciptakan aplikasi web interaktif. Tujuannya adalah untuk memindahkan sebagian besar interaksi pada komputer web surfer atau melakukan pertukaran data dengan server di belakang layar, sehingga halaman web tidak harus dibaca ulang secara keseluruhan setiap kali seorang pengguna melakukan perubahan.

Secara umum code ajax dalam jquery sebagai berikut
```javascript
$.ajax({<name>:<value>, <name>:<value>, ... })
```
Yang mana “name” atau “value” dapat diisi dengan berbagai nilai contoh:
```javascript
<script>
$(document).ready(function(){
    $("#buttonPanggilAjax").click(function(){
        $.ajax({
           url: "example.com", // url yang akan dipanggil
           Data: { data1:”contoh1” , data2:”contoh2 } // data yang akan dikirim ke example.com
           dataType: “json” // atau apapun tipe data yang diharapkan didapat dari example.com
           success: function(result){
                 // disini akan berisi code yang akan dieksekusi jika example.com berhasil dipanggil
                 // result merupakan data yang diperoleh dari example.com
            },
           Error: function(xhr, status, error) {
                // disini akan berisi code yang akan dieksekusi jika example.com gagal dipanggil
            }
       });
    });
});
</script>
```

#### How it all goes together

Nah setelah mengenal semua istilah-istilah atau teknologi tersebut marilah kita melihat bagaimana hal tersebut dapat digunakan untuk membuat suatu aplikasi web. Dalam hal ini suatu aplikasi dapat berkomunikasi dengan aplikasi lainnya dengan membuat suatu interface berupa web services yang dapat digunakan oleh aplikasi lainnya.


Lalu pesan seperti apakah yang dikirim antar aplikasi tersebut? Aplikasi tersebut tentunya saling bertukar data dengan aplikasi lain, yang dalam hal ini salah satunya merupakan object JSON seperti yang telah dipelajari sebelumnya.


Lalu, bagaimana dengan AJAX? Seperti yang telah dijelaskan sebelumnya, AJAX pada dasarnya merupakan suatu cara untuk mengupdate bagian suatu website dengan pemanggilan dari client secara dinamis yang dijalankan oleh browser berdasarkan perintah yang biasanya berupa script javascript.

Nah dalam hal ini AJAX contohnya dapat dipakai suatu website untuk memanggil suatu API dan mengisi bagian atau melakukan update yang dibutuhkan dengan lebih dinamis dan tanpa memerlukan user untuk melakukan request dan mereload keseluruhan halaman.

Contoh Penggunaan

Pada contoh kali ini kita akan melihat contoh pada website traveloka. Dimana secara garis besar kita dapat melihat server-side backend traveloka sebagai satu web service (yang pada kenyataannya, traveloka memiliki infrastruktur microservices yang kompleks dan tidak akan dibahas salam tutorial ini) dan diakses oleh web front-end yang di render oleh browsermu.

Untuk itu lakukanlah tahap berikut ini
Buka halaman https://www.traveloka.com/en/kereta-api
Klik kanan > inspect element > networks (centang opsi preserve log)
Lakukan pencarian kereta dengan UI yang ada
Perhatikan bahwa walaupun tampilan telah ter-render terdapat loading bar dan hasil pencarianmu tidak langsung ter-load.
Namun setelah itu hasil pencarian akan terupdate pada tampilan web tersebut, mengapa?
Setelah hasil pencarian keluar, lihatlah tab networks di tampilan inspect element di browsermu dan cari dengan filter “inventory”.
Lihat format body yang digunakan, terlihat familiar bukan?
Kaitkanlah dengan pengetahuanmu mengenai web service, json, dan ajax!


#### Informasi tambahan

Silahkan cari mengenai istilah di bawah ini, istilah-istilah di bawah merupakan istilah yang berhubungan dengan penggunaan teknologi-teknologi di atas dan merupakan trend  industry  yang sedang berkembang saat ini. Pemahamanmu akan isitilah ini akan dapat membantumu untuk lebih mengenal teknologi web masa kini!

- API First Development
- REST API
- Single Page Application

## Cara menggunakan API
1. Pada tutorial lab kali ini, api yang akan kita gunakan untuk latihan adalah api milik fasilkom, yaitu `https://api-dev.cs.ui.ac.id/`. Kalian bisa membuka link tersebut untuk mengetahui cara penggunaannya dan dokumentasi dari api-dev.cs.ui.ac.id itu sendiri.
2. Untuk menggunakan api dari api.cs.ui.ac.id, hal yang kita perlukan adalah access token dan juga client id(kalian bisa melihat informasi detailnya dengan membuka link yang sudah disebutkan diatas). Pada lab ini, Kak Pewe sudah membuatkan helper untuk memudahkan kalian mendapatkan access token maupun client id. Silahkan pelajari script python yang ada pada lampiran.
3. Pada umumnya, terdapat beberapa method yang sering digunakan dalam menggunakan API, yaitu GET, POST, PUT, dan DELETE.
    * `GET` digunakan untuk mengambil data dari API kalian
    * `POST` digunakan untuk membuat data baru di API
    * `PUT` digunakan untuk mengubah data yang sudah ada di API
    * `DELETE` diguanakan untuk menghapus data dari API
Silahkan tambah pengetahuan kalian, google adalah teman kalian yang baik.
4. Contoh penggunaan API api-dev.cs.ui.ac.id adalah sebagai berikut:
    ```
    https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa-list/?access_token=SECRET_TOKEN&client_id=SECRET_CLIENT_ID
    ```
5. Berikut adalah response yang diberikan oleh API api-dev.cs.ui.ac.id
    ```
    {
        "count": 6800,
        "next": "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa-list/?access_token=SECRET_TOKEN&client_id=SECRET_CLIENT_ID&page=2",
        "previous": null,
        "results": [
            ...

            {
                "url": "https://api-dev.cs.ui.ac.id/siakngcs/mahasiswa/1908989055/",
                "npm": "1908989055",
                "nama": "Kak Pewe",
                "alamat_mhs": "Lab.1103 dan Lab.1107",
                "kd_pos_mhs": "99999",
                "kota_lahir": "Depok",
                "tgl_lahir": "2018-12-18",
                "program": [
                    {
                        "url": "https://api-dev.cs.ui.ac.id/siakngcs/program/96554/",
                        "periode": {
                            "url": "https://api-dev.cs.ui.ac.id/siakngcs/periode/35/",
                            "term": 1,
                            "tahun": 2017
                        },
                        "kd_org": "01.00.12.01",
                        "nm_org": "Ilmu Komputer",
                        "nm_prg": "S1 Reguler",
                        "angkatan": 2015,
                        "nm_status": "Aktif",
                        "kd_status": "1"
                        },

                        ...
                    }
                ]
            },
        ...
    }

    ```
    Kenapa ketika kita buka link tersebut kita bisa mendapat data-data diatas? Method apa yang sebenernya digunakan dalam mengakses sebuah web? Silahkan pelajari kembali kalau kalian masih belum mengerti, atau silahkan tanya Dosen atau Kak Pewe yang baik hati.

    Selain itu, kaitkan juga pengetahuan kalian mengenai method tersebut dengan penggunaan ajax.

6. Kalian bisa melihat daftar API yang ada pada api-dev.cs.ui.ac.id dengan membuka link ini
    ```
    https://api-dev.cs.ui.ac.id/siakngcs/?access_token=SECRET_TOKEN_KAMU&client_id=CLIENT_ID_KAMU
    ```
    Silahkan gunakan access token dan client id kalian sendiri. Kalian bisa menggunakan helper yang sudah Kak Pewe buat, atau dengan menggunakan CURL seperti yang ada pada web `api-dev.cs.ui.ac.id`


## Membuat Halaman Daftar Mahasiswa Fasilkom
1. Jangan lupa jalankan virtual environment kalian
2. Buatlah _apps_ baru bernama `lab_7`
1. Masukkan `lab_7` kedalam `INSTALLED_APPS`
1. Buatlah _Test_ baru kedalam `lab_7/tests.py` :
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Buatlah konfigurasi URL di `praktikum/urls.py` untuk `lab_7`
    ```python
        ........
        import lab_7.urls as lab_7

        urlpatterns = [
            .....
            url(r'^lab-7/', include(lab_7, namespace='lab-7')),
        ]
    ```
1. Buatlah konfigurasi URL di `lab_7/urls.py`
    ```python
        from django.conf.urls import url
        from .views import index, add_todo

        urlpatterns = [
             url(r'^$', index, name='index'),
             url(r'^add-friend/$', add_friend, name='add-friend'),
             url(r'^validate-npm/$', validate_npm, name='validate-npm'),
             url(r'^delete-friend/(?P<friend_id>[0-9]+)/$', delete_friend, name='delete-friend'),
             url(r'^get-friend-list/$', friend_list_json, name='get-friend-list')
        ]
    ```
1. Buat sebuah package bernama `api_csui_helper` lalu buat file `csui_helper.py` ke folder package tersebut
    ```python
    import requests
    import os
    import environ

    root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
    env = environ.Env(DEBUG=(bool, False),)
    environ.Env.read_env('.env')
    API_MAHASISWA_LIST_URL = "https://api.cs.ui.ac.id/siakngcs/mahasiswa-list/"


    class CSUIhelper:
        class __CSUIhelper:
            def __init__(self):
                self.username = env("SSO_USERNAME")
                self.password = env("SSO_PASSWORD")
                self.client_id = 'X3zNkFmepkdA47ASNMDZRX3Z9gqSU1Lwywu5WepG'
                self.access_token = self.get_access_token()

            def get_access_token(self):
                try:
                    url = "https://akun.cs.ui.ac.id/oauth/token/"

                    payload = "username=" + self.username + "&password=" + self.password + "&grant_type=password"
                    headers = {
                        'authorization': "Basic WDN6TmtGbWVwa2RBNDdBU05NRFpSWDNaOWdxU1UxTHd5d3U1V2VwRzpCRVFXQW43RDl6a2k3NEZ0bkNpWVhIRk50Ymg3eXlNWmFuNnlvMU1uaUdSVWNGWnhkQnBobUU5TUxuVHZiTTEzM1dsUnBwTHJoTXBkYktqTjBxcU9OaHlTNGl2Z0doczB0OVhlQ3M0Ym1JeUJLMldwbnZYTXE4VU5yTEFEMDNZeA==",
                        'cache-control': "no-cache",
                        'content-type': "application/x-www-form-urlencoded"
                    }

                    response = requests.request("POST", url, data=payload, headers=headers)

                    return response.json()["access_token"]
                except Exception:
                    raise Exception("username atau password sso salah, input : [{}, {}] {}".format(self.username, self.password, os.environ.items()))

            def get_client_id(self):
                return self.client_id

            def get_auth_param_dict(self):
                dict = {}
                acces_token = self.get_access_token()
                client_id = self.get_client_id()
                dict['access_token'] = acces_token
                dict['client_id'] = client_id

                return dict

            def get_mahasiswa_list(self):
                response = requests.get(API_MAHASISWA_LIST_URL,
                                        params={"access_token": self.access_token, "client_id": self.client_id})
                mahasiswa_list = response.json()["results"]
                return mahasiswa_list

        instance = None

        def __init__(self):
            if not CSUIhelper.instance:
                CSUIhelper.instance = CSUIhelper.__CSUIhelper()
    ```
1. Jika kita lihat, pada file `csui_helper.py` terdapat kode seperti
    ```python
    env('SSO_USERNAME')
    env('SSO_PASSWORD')
    ```
    (baca juga: https://github.com/joke2k/django-environ)
    Kode tersebut mengambil variable dari sistem tempat kode tersebut dijalankan. Artinya kita perlu menset variable yang digunakan tersebut di sistem milik kita.
    Silahkan buka heroku > pilih aplikasi kalian > masuk ke menu setting
    Buka bagian Reveal Config Vars, dan isi sesuai data diri kalian. Ada dua hal yang perlu kalian set disini
    * Isi KEY dengan SSO_USERNAME dan isi value dengan username siak kalian
    * Isi KEY dengan SSO_PASSWORD dan isi value dengan password siak kalian
   untuk keperluan localhost, silahkan kalian buat file .env (satu directory dengan file manage.py) tambahkan variable SSO_USERNAME dan SSO_PASSWORD
   contoh file .env
   ```python
   SSO_USERNAME=anang
   SSO_PASSWORD=hermansyah
   ```
   Penggunaan variable dari env ditujukan untuk menjaga kerahasiaan username dan password kalian agar tidak diketahui oleh orang lain.

1. masukan kode berikut pada views.py
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.core import serializers

    from .models import Friend
    from .api_csui_helper.csui_helper import CSUIhelper
    import os
    import json

    response = {}
    csui_helper = CSUIhelper(os.environ.get("SSO_USERNAME", "yourusername"),
                             os.environ.get("SSO_PASSWORD", "yourpassword"))

    def index(request):
        # Page halaman menampilkan list mahasiswa yang ada
        # TODO berikan akses token dari backend dengan menggunakaan helper yang ada

        mahasiswa_list = csui_helper.instance.get_mahasiswa_list()

        friend_list = Friend.objects.all()
        response = {"mahasiswa_list": mahasiswa_list, "friend_list": friend_list}
        html = 'lab_7/lab_7.html'
        return render(request, html, response)

    def friend_list(request):
        friend_list = Friend.objects.all()
        response['friend_list'] = friend_list
        html = 'lab_7/daftar_teman.html'
        return render(request, html, response)

    @csrf_exempt
    def add_friend(request):
        if request.method == 'POST':
            name = request.POST['name']
            npm = request.POST['npm']
            friend = Friend(friend_name=name, npm=npm)
            friend.save()
            data = model_to_dict(friend)
            return HttpResponse(data)

    def delete_friend(request, friend_id):
        Friend.objects.filter(id=friend_id).delete()
        return HttpResponseRedirect('/lab-7/')

    @csrf_exempt
    def validate_npm(request):
        npm = request.POST.get('npm', None)
        data = {
            'is_taken': #lakukan pengecekan apakah Friend dgn npm tsb sudah ada
        }
        return JsonResponse(data)

    def model_to_dict(obj):
        data = serializers.serialize('json', [obj,])
        struct = json.loads(data)
        data = json.dumps(struct[0]["fields"])
        return data
    ```
1. Buatlah _Models_ untuk `Friend` di dalam `lab_7/models.py`
    ```python
        from django.db import models

        class Friend(models.Model):
        	friend_name = models.CharField(max_length=400)
        	npm = models.CharField(max_length=250)
        	added_at = models.DateField(auto_now_add=True)
    ```
1. Jalankan perintah `makemigrations` dan `migrate`

1. Buatlah `lab_7.css` di dalam `lab_7/static/css` (Jika folder belum tersedia, silahkan membuat folder tersebut)
   ```css
   body{
       margin-top: 70px;
   }
   /* Custom navbar style */
   .navbar-static-top {
       margin-bottom: 19px;
   }
   .navbar-default .navbar-nav>li>a {
       cursor: pointer;
   }
   /* Textarea not resizeable */
   textarea {
       resize:none
   }
   ```

1. Buatlah base.html di dalam `lab_7/templates/lab_6/layout` (Jika folder belum tersedia, silahkan membuat folder tersebut)
   ```html
   {% load staticfiles %}
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="description" content="LAB 5">
       <meta name="author" content="{{author}}">
       <!-- bootstrap csss -->
       <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
       <link rel="stylesheet" type="text/css" href="{% static 'css/lab_7.css' %}" />
       <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Droid+Sans:400,700">

       <title>
           {% block title %} Lab 7 {% endblock %}
       </title>
   </head>
   <body>
       <header>
           {% include "lab_7/partials/header.html" %}
       </header>
       <content>
               {% block content %}
                   <!-- content goes here -->
               {% endblock %}
       </content>
       <footer>
           <!-- TODO Block Footer dan include footer.html -->
           {% block footer %}
           {% include "lab_7/partials/footer.html" %}
           {% endblock %}
       </footer>
       <!-- Jquery n Bootstrap Script -->
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
       <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
       {% block javascript %}
       {% endblock %}
   </body>
   </html>
   ```
1. Buatlah `lab_7.html` di dalam `lab_7/templates/lab_7/`
   ```html
    {% extends "lab_7/layout/base.html" %}
    {% block content %}
    <section name="mahasiswa-list" id="mahasiswa-list">
        <div class="container">
            <div class="row">
                <div class="col-md-8 col-lg-8">
                    <h2> Mahasiswa Fasilkom</h2>
                    <div class="list-group">
                        {% if mahasiswa_list %}
                            {% for mahasiswa in mahasiswa_list %}
                                <a class="list-group-item clearfix">
                                    {{ mahasiswa.nama }} ({{ mahasiswa.npm }})
                                    <span class="pull-right">
                            <span class="btn btn-xs btn-default" onClick="addFriend('{{ mahasiswa.nama }}', '{{ mahasiswa.npm }}')">
                                Tambah sebagai teman
                            </span>
                        </span>
                                </a>
                            {% endfor %}
                        {% else %}
                            <div class="alert alert-danger text-center">
                                <strong>Opps!</strong> Tidak ada mahasiswa
                            </div>
                        {% endif %}
                    </div>
                </div>
                <div class="col-lg-4">
                    <h2> Teman Saya </h2>
                    <div class="list-group" id="friend-list">
                        {% if friend_list %}
                            {% for friend in friend_list %}
                                <a class="list-group-item clearfix">
                                    {{ friend.friend_name }} ({{ friend.npm }})
                                </a>
                            {% endfor %}
                        {% else %}
                            <div class="alert alert-danger text-center">
                                <strong>Opps!</strong> Tidak ada teman
                            </div>
                        {% endif %}
                    </div>
                    <form id="add-friend" action="#">
                        {% csrf_token %}
                        <label for="field_npm">npm</label>
                        <input id="field_npm" type="text" name="npm" class="form-control"/>
                        <label for="field_name">name</label>
                        <input id="field_name" type="text" name="name" class="form-control"/>
                        <button type="submit">Tambah</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    {% endblock %}
    ```
1. Tambahkan code javascript berikut pada `lab_7.html` di dalam `lab_7/templates/lab_7/`
    ```html
    ...
    {% block javascript %}
    <script>
        var addFriend = function(nama, npm) {
            $.ajax({
                method: "POST",
                url: "{% url "lab-7:add-friend" %}",
                data: { name: nama, npm: npm},
                success : function (friend) {
                    html = '<a class="list-group-item clearfix">' +
                        friend.friend_name +
                        '</a>';
                    $("#friend-list").append(html)
                },
                error : function (error) {
                    alert("Mahasiswa tersebut sudah ditambahkan sebagai teman")
                }
            });
        };

        $("#add-friend").on("submit", function () {
           name = $("#field_name").val()
           npm = $("#field_npm").val()
            addFriend(name, npm)
            event.preventDefault();
        });

        $("#field_npm").change(function () {
            console.log( $(this).val() );
            npm = $(this).val();
            $.ajax({
                method: "POST",
                url: '{% url "lab-7:validate-npm" %}',
                data: {
                    'npm': npm
                },
                dataType: 'json',
                success: function (data) {
                    console.log(data)
                    if (data.is_taken) {
                        alert("Mahasiswa dengan npm seperti ini sudah ada");
                    }
                }
            });
        });
    </script>
    {% endblock %}
    ```
1. pelajari apa yang dilakukan kode javascript tersebut
1. jalankan webserver kalian


#### Implementasi Ajax
1. buatlah sebuah halaman yang menampilkan daftar teman

1. gunakan file pendukung 'daftar-teman.html'
    ```html
    {% extends "lab_7/layout/base.html" %}

    {% block content %}
        <section name="friend-list" id="friend-list">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 col-lg-8">
                        <h2> friend Fasilkom</h2>
                        <div id="friend-list" class="list-group">

                        </div>
                    </div>
                </div>
            </div>
        </section>
    {% endblock %}
    {% block javascript %}
        <script>
            $( document ).ready(function () {
                {# lengkapi pemanggilan ajax berikut untuk mengambil daftar teman yang ada di database #}
                $.ajax({
                    method: "GET",
                    url: #URL untuk mendapatkan list teman],
                    success: function (response) {
                        #tampilkan list teman ke halaman
                        #hint : gunakan fungsi jquery append()
                    },
                    error: function(error){
                        #tampilkan pesan error
                    }
                });
            });
        </script>
    {% endblock %}
    ```
1. implementasi pemanggilan ajax tersebut

## Checklist

### Mandatory
1. Membuat halaman untuk menampilkan semua mahasiswa fasilkom
    1. [ ] Terdapat list yang berisi daftar mahasiswa fasilkom, yang dipanggil dari django model.
    2. [ ] Buatlah tombol untuk dapat menambahkan list mahasiswa kedalam daftar teman (implementasikan menggunakan ajax).
    3. [ ] Mengimplentasikan validate_npm untuk mengecek apakah teman yang ingin dimasukkan sudah ada didalam daftar teman atau belum.
    4. [ ] Membuat pagination (hint: salah satu data yang didapat dari kembalian api.cs.ui.ac.id adalah `next` dan `previous` yang bisa digunakan dalam membuat pagination)
2. Membuat halaman untuk menampilkan daftar teman
    1. [ ] Terdapat list yang berisi daftar teman, data daftar teman didapat menggunakan ajax.
    2. [ ] Buatlah tombol untuk dapat menghapus teman dari daftar teman (implementasikan menggunakan ajax).
3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%


### Additional

1. Membuat halaman yang menampilkan data lengkap teman 
    1. [ ] Halaman dibuka setiap kali user mengklik salah satu teman pada halaman yang menampilkan daftar teman
    1. [ ] Tambahkan google maps yang menampilkan alamat teman pada halaman informasi detail (hint: https://developers.google.com/maps/documentation/javascript/)
