# Lab 2: Pengenalan _Django Framework_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Mengerti Struktur _Django Project_
- Mengerti bagaimana alur _Django_ menampilkan sebuah _webpage_ 
- Mengerti konfigurasi yang ada pada _settings.py_

## Pengenalan

_Django_ merupakan salah satu _framework_ yang menggunakan bahasa pemrograman _python_.
_Framework_ sangat berguna dalam pengembangan web karena sudah menyediakan komponen-komponen 
yang dibutuhkan untuk membuat dan menjalankan suatu web, tanpa harus mulai dari nol. 
Sebelum memulai pengembangan web menggunakan Django, penting untuk memahami apa itu `virtual environemnt` (virtualenv).
Virtual environment (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan _package_ yang di _install_  
pada setiap _Django project_ sehingga perubahan yang dilakukan pada satu _project_ tidak mempengaruhi _project_ lainnya. 
Dengan kata lain, setiap _Django project_ sebaiknya memiliki _virtualenv_ nya sendiri. 

> Pastikan saat pembuatan virtualenv, yang digunakan adalah python versi 3 (cek dengan `python --version` )
>
> Sebelum memulai pengembangan web, biasakan untuk selalu mengaktifkan virtualenv terlebih dahulu.
> 

## Struktur _Django Project_

`django-admin.py` adalah _script_ yang digunakan untuk pembuatan _Django project_. Perintah untuk membuat suatu _project_

``` django-admin.py startproject <NAMA-PROJECT> ```

> Ganti `<NAMA-PROJECT>` dengan nama yang kalian inginkan, misalkan Lab-PPW-2017

Struktur project yang dihasilkan, 
1. `virtualenv` sebagai sub-dir _project_ <NAMA-PROJECT>

``` python
- <NAMA-PROJECT>
    - manage.py
    - <NAMA-PROJECT>
        __init__.py
        settings.py
        urls.py
        wsgi.py
    - <django-apps-1>
        ...
    - <django-apps-2>
        ...
    - virtualenv
        ...
```
2. `virtualenv` satu level dengan _project_ <NAMA-PROJECT>

```python
- virtualenv
    ...
- <NAMA-PROJECT>
    - manage.py
    - <NAMA-PROJECT>
        __init__.py
        settings.py
        urls.py
        wsgi.py
    - <django-apps-1>
        ...
    - <django-apps-2>
        ...    
```

> Direktori virtualenv bisa berada dalam direktori utama _project_ `<NAMA-PROJECT>` (sebagai sub-direktori) 
> atau bisa di luar, satu level dengan direktori utama _project_ `<NAMA-PROJECT>`). 
>
> Jangan lupa untuk memasukkan `virtualenv` ke dalam `.gitignore`

Perhatikan bahwa direktori dengan nama `<NAMA-PROJECT>` ada dua buah.  
Direktori yang pertama adalah direktori utama _project_ , sementara direktori yang kedua adalah
direktori konfigurasi atau pengaturan _project_ yang di dalamnya terdapat berkas `settings.py`. 

`django-apps-1` dan `django-apps-2` merupakan `apps` milik Django. Contoh yang sudah ada ialah `lab_1` dan `lab_2`. 
Dalam satu _project_ bisa terdapat banyak `apps`. Untuk membuat suatu app, gunakan perintah

``` python manage.py startapp <app-name> ```

> ganti` <app-name>` menggunakan nama sesuai kebutuhan/keinginan kalian, misalkan `lab_x`. 
> sebelum menjalankan perintah ini, pastikan sudah berada satu direktori dengan berkas `manage.py`. 
>
> Coba perintah `ls` (linux) atau `dir` (windows) 

Struktur umum dari suatu `apps` ialah :
```python
    - <app-name>
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        - migrations
            ...
        - templates
            ...
```

> Suatu `app` dianggap aktif atau terpakai jika `app` tersebut didaftarkan di pengaturan `INSTALLED_APPS`
> pada berkas `settings.py` (ada pada direktori pengaturan _project_, yang nama direktorinya sama dengan nama _project_ Django)

Secara _default_ , tidak ada berkas `urls.py` karena Django memberikan kebebasan untuk membuat _routing_ sesuai kebutuhan pengembang.
Namun untuk _best practice_ dan kemudahan pengembangan, berkas `urls.py` dibuat manual untuk setiap `app`. Berkas `urls.py` satu level
(satu direktori) dengan berkas `views.py`

Selain itu, untuk menyimpan berkas `HTML`  (misalkan `index.html`) biasanya dibuat suatu direktori bernama `templates` di 
dalam direktori `<app-name>`, jadi struktur dari suatu `app` nantinya akan menjadi 

```python
    - <app-name>
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        urls.py
        - migrations
            ...
        - templates
            ...
```

> Apa beda `Project` dan `App` ? _Project_ adalah kumpulan konfigurasi dan beberapa app (aplikasi) untuk suatu website tertentu. 
> Sedangkan _App_ adalah suatu aplikasi web yang memiliki fungsi/tugas tertentu, misalkan sebagai database atau sebagai aplikasi survei sederhana.
> Satu _project_ dapat memiliki banyak _app_, dan satu _app_ dapat digunakan di banyak _project_.
> 
> Tutorial pembuatan Django _project_ : <cite> https://docs.djangoproject.com/en/1.11/intro/tutorial01/ </cite>

Sekilas tentang berkas `settings.py` , pada berkas ini terdapat _section_ `INSTALLED_APPS` yang berfungsi untuk 
mendaftarkan aplikasi yang akan dipakai/dijalankan pada suatu _project_.
Contohnya, mendaftarkan `app` bernama "lab_ppw" ke INSTALLED_APPS : 

```python
INSTALLED_APPS = [
    ...
    lab_1,
    lab_ppw,
]
```


> jika "sedang" tidak ingin menggunakan suatu `app`, daripada menghapus folder `app` tersebut, kamu bisa 
> menon-aktifkan `app` tersebut dengan menghapusnya dari _INSTALLED_APPS_


## Routing pada Django
Routing dapat diumpamakan sebagai suatu pemetaan. URL (Uniform Resource Locator) atau sederhananya adalah suatu alamat web.
`http://localhost:8000` merupakan contoh sederhana dari suatu URL. `http://localhost` adalah alamat utamanya, sedangkan `8000` 
adalah _port_ yang digunakan. Django memiliki python _module_ bernama `URLconf` (URL configuration) berisi sekumpulan 
pola atau _pattern_ yang Django akan coba cocokkan untuk menemukan `views` (tampilan) yang benar. 

> Django menggunakan _regular expression_ atau _regex_ untuk melakukan pencocokan antara URL dengan `views` (tampilan).
> Kalau penasaran bagaiman membuat _regex_ pada Python , coba cek [link](https://docs.python.org/3/howto/regex.html) berikut 

Perhatikan struktur _project_ Django, terdapat sub-dir dengan nama sama persis dengan nama project yang dibuat, dengan struktur : 

```python
<NAMA-PROJECT>
    __init__.py
    settings.py
    urls.py
    wsgi.py
```

Secara sederhana, format penulisan utk URL pada Django ialah `url(regex, view, kwargs=None, name=None)`

- regex ialah _pattern_ yang akan dicocokkan 
- `view` ialah fungsi yang untuk memproses _request_ dan mengatur tampilan.
- _kwargs_ dan _name_ saat ini bisa diabaikan/dikosongkan

> Untuk mengetahui lebih lanjut format penulisan urls, cek [link] (https://docs.djangoproject.com/en/1.11/_modules/django/conf/urls/#url) berikut 

Berkas `urls.py` pada direktori ini adalah contoh URLconf yang disediakan oleh Django, yang dapat digunakan untuk 
melakukan `routing` ke `apps` Django lainnya. Contoh untuk membuat `routing` ke `app` lain , berdasarkan `lab_1` yang sudah dikerjakan (cek repo):

```python 
...
from django.conf.urls import url, include
import lab_1.urls as lab_1
urlpattern = [
    ...
    url(r'^lab-1/', include(lab_1, namespace='lab-1')),
    ...
]
```
> Note: Tanda titik tiga `...` pada kode di atas sebagai tanda bahwa isinya bisa apa saja, sesuai kebutuhan.  

Perhatikan bahwa berkas `urls.py` pada `app` Django tidak dibuat secara otomatis oleh Django, melainkan dibuat secara manual.
Pada contoh di atas, dalam direkotri `lab_1` diasumsikan ada berkas `urls.py`. Tanda dot (titik) sebagai penanda
untuk mengakses isi direktori tersebut. 

Penjelasan ringkas: 

- Baris kode `url(r'^lab-1/', include(lab_1, namespace='lab-1'))`, menggunakan _regex_ `^` , yang artinya untuk setiap
URL dengan awalan `lab-1/` yang menangani URL tersebut adalah berkas `lab_1.urls`.
- alamat `http://localhost/lab-1/` akan ditangani oleh berkas `lab_1.urls` 
- `import lab_1.urls as lab_1` --> `lab_1.urls` diganti namanya dengan `lab_1`, 
 sehingga baris kode `include(lab_1, ... )` tetap memanggil berkas `lab_1.urls`

> sumber kode  : https://gitlab.com/PPW-2017/ppw-lab/blob/master/lab_1/urls.py

Selanjutnya untuk melihat penggunaan `views`, kita harus melihat isi berkas dari `lab_1.urls` : 

```python
from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
]
```
Penjelasan ringkas : 
- _regex_ pada url(`r'^$'`) berarti _input_ apapun akan dialihkan ke sebuah `views` bernama `index`
- `index` juga dapat diganti dengan `views.index` tapi sama saja, fungsinya untuk memproses tampilan

Pada berkas `views.py` diasumsikan (dan seharusnya) ada fungsi bernama `index` atau `def index(request):`.
Pada berkas `views.py` ini, juga akan diatur bagaimana _request_ akan diproses sebelum ditampilkan. 
Perhatikan fungsi `render` yang ada pada berkas `views.py`, terdapat berkas HTML.
Direktori `templates` berfungsi untuk menyimpan berkas HTML yang dipanggil oleh `views`, jadi
pastikan berkas tersebut ada dan namanya sesuai untuk menghindari kesalahan.

> Untuk memastikan hal tersebut, cek penggunaan `views` pada https://gitlab.com/PPW-2017/ppw-lab/blob/master/lab_1/views.py 
>
> INGAT: penulisan variabel, parameter, fungs, dsb, pada Django _case-sensitif_. Jadi harus teliti dalam menulisakan kode
>
> Penjelasan ringkas mengenai URL Django : <cite> https://tutorial.djangogirls.org/en/django_urls/ </cite>
>
> Penjelasan lebih detail bagaimana URLconf bekerja :  <cite> https://docs.djangoproject.com/en/1.11/topics/http/urls/ </cite>

## Cara Menampilkan _Webpage_

Pada lab ini anda telah disediakan sebuah _template_ `apps`  Django. Tugas Anda adalah membuat sebuah _Landing Page_ 
dengan _template_ yang sudah diberikan, lalu menambahkan sebuah `apps` baru yang akan menjadi _Page_ tambahan
untuk _webpage_ kalian

1. Bukalah folder `lab_2` lalu isilah variable `landing_page_content` dalam `views.py` dengan deskripsi singkat yang biasanya ada
di sebuah `landing page`

    > Jika anda tidak tahu apa itu `landing page` lihatlah [link](https://unbounce.com/landing-page-articles/what-is-a-landing-page/) berikut

2. Bukalah file `urls.py` didalam folder `lab_2`. Disini akan ditulis konfigurasi URL yang akan diproses. Dalam hal ini 
 kalian harus menambahkan URL untuk menampilkan _Landing Page_ dengan menggunakan _template_ yang sudah disediakan. 
 Ubah `urls.py` dengan kode dibawah ini agar pada saat _request_ diberikan pada `<HOSTNAME>/lab-2/` maka _Landing Page_ yang ada pada
 [index_lab2.html](templates/index_lab2.html) bisa dimunculkan
 
```python
    from django.conf.urls import url
    from .views import index
    #url for app
    urlpatterns = [
        url(r'^$', index, name='index'),
    ]
```

3. Jalankan Django secara lokal :

    > python manage.py runserver 8000

4. Selamat, kalian sudah berhasil menampilkan _Landing Page_ kalian sendiri

    > Kalian mungkin sadar, ada tulisan yang dapat di klik. Jika di klik, maka halaman _web_
    > akan mengarah ke `<HOSTNAME>/lab-2-addon/`. Ini adalah hal selanjutnya yang harus kalian 
    > implementasikan
    
5. `commit` dan `push` pekerjaan kalian ke repo masing - masing

## Checklist

1. Menampilkan Halaman _Landing Page_
    1. [ ] Isi variabel `landing_page_content` sehingga menjadi _Landing Page_ yang layak (Min 30 karakter)
    2. [ ] Buatlah konfigurasi URL dalam _file_ `lab_2/urls.py` sehingga _Landing Page_ bisa diakses dengan URL `<HEROKU_APP_HOST>/lab-2/`
        > contoh : djangoppw.herokuapp.com/lab-2/
2. Membuat _Django Apps_ baru bernama *lab_2_addon* lalu lakukan konfigurasi pada `views.py`
    1. [ ] Buatlah sebuah `app` baru (Hint: Jalankan _command_ `python manage.py help`)
    2. [ ] Isilah `views.py` pada `app` baru dengan kode berikut, lalu ubah variabel yang belum sesuai
    
```python
    from django.shortcuts import render
    from lab_1.views import mhs_name, birth_date
    #Create a list of biodata that you wanna show on webpage:
    #[{'subject' : 'Name', 'value' : 'Igor'},{{'subject' : 'Birth Date', 'value' : '11 August 1970'},{{'subject' : 'Sex', 'value' : 'Male'}
    #TODO Implement
    bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
    {'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},\
    {'subject' : 'Sex', 'value' : ''}]
    
    def index(request):
        response = {}
        return render(request, 'description_lab2addon.html', response)
```
4. Berikanlah sebuah _folder templates_ pada `apps lab_2_addon` untuk menampung semua _file_ HTML yang
 akan dijalankan didalam `apps lab_2_addon`:
    1. [ ] Buatlah _folder templates_ di dalam `apps lab_2_addon`
    2. [ ] Pindahkan _file_ `lab_2/templates/description_lab2addon.html` ke dalam _folder templates_
     yang ada di `apps lab_2_addon`
5. Buatlah sebuah konfigurasi URL sehingga `description_lab2addon.html` bisa ditampilkan sesuai dengan yang diharapkan
    1. [ ] Ubah file `urls.py` yang ada didalam _folder_ `lab_2_addon` dan `praktikum` sehingga URL `<HEROKU_APP_HOST>/lab-2-addon/`
    bisa menampilkan halaman `description_lab2addon.html`
    2. [ ] Ubah _section_ INSTALLED_APPS sehingga `apps lab_2_addon` dapat dikenali sebagai _Django Apps_ yang aktif (Tanpa melakukan langkah ini
    maka halaman `description_lab2addon.html` tidak bisa ditampilkan melalui URL yang sudah dibuat di `urls.py`)
    3. [ ] Tampilkan halaman _Landing Page_ jika ada _request_ yang datang pada Root URL _website_ kalian
        >Ketika mengakses `<HEROKU_APP_HOST>/` maka _Landing Page_ akan tampil (Hint: Gunakan RedirectView)
    4. [ ] Isilah _file_ `lab_2_addon/tests.py` dengan cara memindahkan `class Lab2AddonUnitTest` beserta semua
    _Test Case_ yang ada lalu aktifkan _Test Case_ tersebut dengan menghilangkan `skip` di atas setiap _Test Case_.
    Import semua `library`, `function` atau `variabel` yang dibutuhkan agar _Test Case_ bisa dijalankan
        
6. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab`
    di [README.md](https://gitlab.com/PPW-2017/Draft-Lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%