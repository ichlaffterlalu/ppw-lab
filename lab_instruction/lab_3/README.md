# Lab 3: Pengenalan _Setting_ PostgreSQL di Heroku, pengenalan _models_ dan TDD

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Mengaktifkan PostgreSQL di Heroku 
- Mengerti penggunaan _models_ pada _Django Project_ 
- Disiplin TDD dalam pengembangan _Web Application_


## Menambahkan _Addon_ PostgreSQL kedalam Aplikasi Heroku (Info Tambahan)

Untuk dapat menggunakan Heroku _command prompt_  (heroku-cli) _install_ terlebih dahulu
dengan mengikuti petunjuk pada [link](https://devcenter.heroku.com/articles/heroku-cli) berikut. 

Setelah proses _install_ selesai, buka _terminal_ atau _command prompt_ (disarankan menggunakan _cmd_ pada Windows)
dan ketikkan `heroku` untukk memastikan bahwa _heroku-cli_ sudah terpasang dengan benar. 

Setiap kalian membuat aplikasi di Heroku, maka secara otomatis Heroku akan membuatkan sebuah PostgreSQL _Database_ yang bisa kalian gunakan untuk aplikasi kalian.

Untuk cek keberadaan _database_ , jalankan perintah berikut di `Command Prompt` :

> heroku addons

Kalian bisa melihat contoh tampilan yang akan dikeluarkan oleh perintah tersebut di
[link](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) berikut 

Bilamana tampilan tersebut tidak muncul, maka kalian harus membuat secara manual _Database_ PostgreSQL:

> heroku addons:create heroku-postgresql:hobby-dev --app <YOURAPPNAME>

## Django _Models_ dan _Migrations_ 

_Model_ pada Django adalah suatu sumber informasi terdefinisi dan detail mengenai data yang disimpan, lengkap dengan karakteristiknya
nama kolom; tipe data; dst. Secara umum, setiap _model_ dipetakan ke dalam satu tabel _database_.
Berkas `models.py` dibuat secara otomatis untuk setiap `app` Django yang dibuat. 

> Penjelasan lebih lanjut dan contoh _Model_ pada Django, cek [link] (https://docs.djangoproject.com/en/1.11/topics/db/models/) berikut

_Migrations_ adalah cara Django untuk menerapkan perubahan yang dilakukan pada _Models_ (tambah, hapus, ubah kolom, dsb) ke dalam _database_. 
Ada beberapa perintah yang berkaitan dengan _migrations_ dan skema _database_ di Django, antara lain :  `migrate` dan `makemigrations` .

> Perhatikan bahwa di dalam setiap direktori `app` Django terdapat direktori bernama _migrations_ . Direktori ini berisi berkas-berkas yang menyimpan
data _migrations_ yang sudah dilakukan. 

`makemigrations` digunakan untuk mencatat dan membuat _migrations_ yang dilakukan pada _models_ (berkas `models.py`).

`migrate` digunakan untuk menerapkan _migrations_ yang ada. 

Perhatikan bahwa perintah untuk menerapakan _migrations_ yang ada adalah `migrate` BUKAN `makemigrations`.

> Penjelasan lebih lanjut mengenai _Migrations_ pada Django cek [link] (https://docs.djangoproject.com/en/1.11/topics/migrations/) berikut

## Mengubah tampilan _Landing Page_ dengan menambahkan _Navigation Bar_

1. _Replace file_ description_lab2addon.html di dalam apps `lab_2_addon` dengan yang ada di  folder templates di
 _root folder_
2. Jalankan Django secara lokal :

    > python manage.py runserver 8000 

Maka kalian bisa melihat, terdapat _Navigation Bar_ pada _Landing Page_ Kalian

## Membuat Halaman _Diary_ (Menggunakan Disiplin TDD)

1. _Update Workspace_ kalian dengan melakukan `git pull upstream master`. Pastikan variable *upstream* sudah berisi _value_ yang sesuai yaitu: 'https://gitlab.com/PPW-2017/ppw-lab.git'. Untuk memeriksanya bisa jalankan perintah:
    ```git
    git remote -v
    ```

   > Bila belum ada silahkan ikuti instruksi [Initial Setup](../Readme.md) di berkas 'Readme.md' pada _root directory_


2. Jalankan _Virtual Environment_ kalian
3. _Install tools_ terbaru dari `requirement.txt`
    ```python
    pip install -r requirement.txt
    ```
4. Buatlah sebuah apps baru bernama `lab_3`
5. Pindahkan berkas HTML `to_do_list.html` ke _folder_ `templates` yang berada dalam `lab_3`

    > Buat _folder_ templates bilamana di dalam `lab_3` belum tersedia

6. Masukkan `lab_3` ke dalam INSTALLED_APPS di dalam `praktikum/settings.py`
7. Masukkan _Test Case_ Berikut ke dalam `lab_3/tests.py`
    ```python
        from django.test import TestCase, Client
        from django.urls import resolve
        from .views import index

        class Lab3Test(TestCase):
            def test_lab_3_url_is_exist(self):
                response = Client().get('/lab-3/')
                self.assertEqual(response.status_code,200)

            def test_lab_3_using_to_do_list_template(self):
                response = Client().get('/lab-3/')
                self.assertTemplateUsed(response, 'to_do_list.html')

            def test_lab_3_using_index_func(self):
                found = resolve('/lab-3/')
                self.assertEqual(found.func, index)
    ```
    Berikut adalah _Test Case_ yang akan memastikan bahwa URL `<YOURHOSTNAME>/lab-3/` **bisa diakses, menggunakan fungsi index di dalam `views.py`, dan
    menggunakan template yang bernama `to_do_list.html`**

8. Jika kalian menjalankan _test_ secara lokal, maka kalian bisa melihat terjadi _error_ . Gunakan perintah 

    > python manage.py test

9. Untuk men-_solve_ semua _Test Case_, maka pertama - tama kalian harus membuat **konfigurasi URL**. Berikan 
konfigurasi URL untuk `lab_3` (Buat berkas `urls.py` di dalam `lab_3`, lalu masukkan kode berikut) :
    ```python
        from django.conf.urls import url
        from .views import index
        #url for app
        urlpatterns = [
            url(r'^$', index, name='index'),
        ]
    ```
10. Masukkan kode berikut kedalam `lab_3/views.py` untuk dapat menampilkan berkas `to_do_list.html`:
    ```python
        from django.shortcuts import render
        # Create your views here.
        diary_dict = {}
        def index(request):
            return render(request, 'to_do_list.html', {'diary_dict' : diary_dict})
    ```
11. Sisipkan kode berikut kedalam konfigurasi URL untuk `lab_3` ke dalam `praktikum/urls.py`:
    ```python
        ...........
        import lab_3.urls as lab_3
        ...........

        urlpatterns = [
            .............
            url(r'^lab-3/', include(lab_3,namespace='lab-3')),
        ]
    ```
    `.....` menandakan kode kalian yang sudah ada, sehingga kode yang tertulis disini cukup kalian sisipkan bukan untuk di _copy-paste_

12. Silahkan jalankan _test_ kalian lagi maka kalian bisa melihat semua _Test Case_ akan ter-_solved_

    > `python manage.py test`
    
13. Untuk membuat fitur yang akan menambahkan dan menampilkan _list_ aktifitas maka pertama - tama kalian harus membuat 
**models** terlebih dahulu. Sisipkan _Test Case_ berikut kedalam `lab_3/tests.py` :
    ```python
        .........
        from .models import Diary
        from django.utils import timezone

        class Lab3Test(TestCase):
            ......................
            def test_model_can_create_new_activity(self):
                #Creating a new activity
                new_activity = Diary.objects.create(date=timezone.now(),activity='Aku mau latihan ngoding deh')

                #Retrieving all available activity
                counting_all_available_activity = Diary.objects.all().count()
                self.assertEqual(counting_all_available_activity,1)
    ```
14. Jalankan _Test Case_ kalian, maka akan kembali muncul _Error_ pada _Test Case_

    > Trivia
    >
    > Inilah langkah - langkah TDD yang nantinya akan kalian lakukan. Untuk membuat fitur, kalian membuat _Test Case_
    terlebih dahulu, dan ketika dijalankan _Test Case_ tersebut harus _Error_ (RED). Selanjutnya kalian harus membuat
    suatu fungsi yang menyelesaikan _Test Case_ tersebut (GREEN)
    
15. Buatlah sebuah **models** bernama `Diary` di dalam berkas `lab_3/models.py`:
    ```python
        from django.db import models

        # Create your models here.
        class Diary(models.Model):
            date = models.DateTimeField()
            activity = models.TextField(max_length=60)
    ```

16. Jalankan _Test Case_ kalian (`python manage.py test`), maka akan kembali muncul _Error_ pada _Test Case_

    > Loh Kenapa?
    >
    > Hal ini dikarenakan kalian belum melakukan _Database migrations_ dan proses _migrate_ 
    >
    > Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk menerapkan 
    > perubahan yang sudah kamu lalukan pada semua berkas `models.py`     

17. Buka kembali berkas `lab_3/tests.py` lalu tambahkan kode berikut pada baris paling akhir :
    ```python
        ........
        class Lab3Test(TestCase):
            ........
            def test_can_save_a_POST_request(self):
            response = self.client.post('/lab-3/add_activity/', data={'date': '2017-10-12T14:14', 'activity' : 'Maen Dota Kayaknya Enak'})
            counting_all_available_activity = Diary.objects.all().count()
            self.assertEqual(counting_all_available_activity, 1)

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['location'], '/lab-3/')

            new_response = self.client.get('/lab-3/')
            html_response = new_response.content.decode('utf8')
            self.assertIn('Maen Dota Kayaknya Enak', html_response)
    ```
18. Setelah itu jalankan kembali _Test Case_ ( `python manage.py test` ) , akan muncul _error_.
     > Contoh potongan kode _error_ yang muncul seperti
     > from .views import index, add_activity
     > 
     > ImportError: cannot import name 'add_activity'

19. Buka berkas `lab_3/views.py` dan tambahkan baris kode berikut : 
    ```python
    from .models import Diary
    from datetime import datetime
    import pytz
    ....
    def add_activity(request):
        if request.method == 'POST':
            date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
            Diary.objects.create(date=date.replace(tzinfo=pytz.UTC),activity=request.POST['activity'])
            return redirect('/lab-3/')
    ```
20. Kemudian pada berkas `lab_3/urls.py` tambahkan kode berikut : 
     ```python
    ...
    from .views import add_activity
    urlpatterns = [
        ...
        url(r'add_activity/$', add_activity, name='add_activity'),
    ]
     ```
21. Jalankan kembali _test_ untuk memastikan bahwa akan muncul _Error_

    >Hal ini dikarenakan data kalian sudah bisa dibuat di _Database_, namun data tersebut
    belum ditampilkan ke halaman depan. Untuk itu kita harus menampilkan kembali semua data yang sudah
    kita simpan di _Database_ 

22. Untuk menampilkan data yang sudah tersimpan di _Database_ maka ubah kode yang ada
di `lab_3/views.py` sehingga menjadi seperti berikut:

    ```python
    from django.shortcuts import render, redirect
    from .models import Diary
    from datetime import datetime
    import pytz
    import json
    # Create your views here.
    diary_dict = {}
    def index(request):
        diary_dict = Diary.objects.all().values()
        return render(request, 'to_do_list.html', {'diary_dict' : convert_queryset_into_json(diary_dict)})
    
    def add_activity(request):
        if request.method == 'POST':
            date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
            Diary.objects.create(date=date.replace(tzinfo=pytz.UTC),activity=request.POST['activity'])
            return redirect('/lab-3/')
    
    def convert_queryset_into_json(queryset):
        ret_val = []
        for data in queryset:
            ret_val.append(data)
        return ret_val
    ```

23. Coba jalankan _test_ kalian dan (seharusnya) _test_ kalian akan **passed**
    > ....................
    >
    > Ran 19 Test Ok

## Checklist

1. Semua Halaman di URL `/lab-2/`, `/lab-2-addon/`, dan `/lab-3/` memiliki _Navigation Bar_
    1. [ ] Terdapat `base.html` di dalam _folder_ templates di _Root Folder_
    2. [ ] Menggunakan `index_lab2.html` yang terbaru
    3. [ ] Menggunakan `description_lab2addon.html` yang terbaru
2. Membuat Fitur **Menulis Kegiatan** dan **Menampilkan Semua Kegiatan** di Halaman _Diary_ :
    1. [ ] Membuat _apps_ baru bernama `lab_3`
    2. [ ] Masukkan `lab_3` kedalam INSTALLED_APPS
    3. [ ] Implementasi _Test Case_ di `lab_3/tests.py`
    4. [ ] Implementasi `lab_3/views.py`
    5. [ ] Implementasi konfigurasi URL di `lab_3/urls.py`
    6. [ ] Ubah `praktikum/urls.py` sehingga konfigurasi `lab_3/urls.py` bisa diakses
3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab`
    di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%

## Challenge Checklist

Cukup kerjakan salah satu nya saja:
1. [ ] Perbaikan Warna dan layout yang lebih rapi lagi untuk tampilan _Website_
2. [ ] Berikan _Input Validation_, ketika Input untuk tanggal tidak sesuai format, maka data tidak tersimpan
(Saat ini yang dilakukan oleh program adalah memberikan _stacktrace error_. Hal ini biasanya terjadi di _browser_ Mozilla)
Validasi perlu dilakukan selain di browser (HTML5 atau Java-Script) dan
3. [ ] _Input Validation_ di-server dalam bentuk
exception handling (sebagai bagian dari _best-practices_ yang salah satu manfaatnya
untuk antisipasi _injection_).