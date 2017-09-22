# Lab 4: Pengenalan _HTML5_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti :

- Mengerti susunan tag pada _HTML5_
- Mengetahui berbagai jenis tag _HTML5_
- Mengerti syntax _for_ dan _if_ pada templating _Django_

## Pengenalan

Silahkan pelajari https://www.html-5-tutorial.com/all-html-tags.htm

## _Django_ Templating

#### Django Template Language (DTL)

Django Template Language dirancang untuk mempermudah pekerjaan dengan HTML. Template sendiri sederhananya adalah sebuah file teks. Template mengandung variabel, yang nilainya dapat dirubah saat dievaluasi. Dan tag yang mengontrol template itu sendiri. berikut adalah contoh dari DTL:
```html
    {% extends "base_generic.html" %}
    {% block title %}{{ section.title }}{% endblock %}
    
    {% block content %}
    <h1>{{ section.title }}</h1>
    
    {% for story in story_list %}
    <h2>
      <a href="{{ story.get_absolute_url }}">
        {{ story.headline|upper }}
      </a>
    </h2>
    <p>{{ story.tease|truncatewords:"100" }}</p>
    {% endfor %}
    {% endblock %}
```
    
#### Displaying Variables

Variabel terlihat seperti ini: **{{ variable }}**. Ketika template menemukan variabel, variabel tersebut akan dievaluasi dan digantikan dengan hasilnya. Nama variabel terdiri dari kombinasi karakter alfanumerik dan garis bawah ("_"). Gunakan titik (".") untuk mengakses atribut sebuah variabel.

#### Tags

Tag terlihat seperti ini: **{% tag%}**. Tag lebih kompleks daripada variabel, beberapa tag menghasilkan suatu keluaran teks, beberapa mengontrol loop atau logika, dan memuat informasi eksternal ke dalam template.

Beberapa tag memerlukan tag awal dan akhir. DTL memiliki banyak tag *built-in* pada template. Anda dapat membaca selengkapnya di [tags yang ada pada DTL](https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#ref-templates-builtins-tags).

**If, Elif, Else**

if, elif dan else dipakai untuk mengevaluasi suatu variabel dan mengeluarkan output ataupun menjalankan suatu perintah. Berikut adalah contoh penggunaan if, elif dan else.
```html
    {% if athlete_list %}
        Number of athletes: {{ athlete_list|length }}
    {% elif athlete_in_locker_room_list %}
        Athletes should be out of the locker room soon!
    {% else %}
        No athletes.
    {% endif %}
```

**For**

for dipakai 
```html
    <ul>
    {% for athlete in athlete_list %}
        <li>{{ athlete.name }}</li>
    {% endfor %}
    </ul>
```

**Block, Extend dan Include**



## Membuat halaman _Home Page_ Baru

1. Buatlah _apps_ baru bernama `lab_4`
1. Masukkan `lab_4` kedalam INSTALLED_APPS
1. Buatlah _Test_ baru kedalam `lab_4/tests.py` :
    ```python
        from django.test import TestCase
        from django.test import Client
        from django.urls import resolve
        from django.http import HttpRequest
        from .views import index, about_me, landing_page_content
        # Create your tests here.
        
        class Lab4UnitTest(TestCase):
            def test_lab_4_url_is_exist(self):
                response = Client().get('/lab-4/')
                self.assertEqual(response.status_code, 200)
             
            def test_about_me_more_than_6(self):
               self.assertTrue(len(about_me) >= 6)
            
            def test_lab4_using_index_func(self):
                found = resolve('/lab-4/')
                self.assertEqual(found.func, index)
              
            def test_landing_page_is_completed(self):
                request = HttpRequest()
                response = index(request)
                html_response = response.content.decode('utf8')
        
                #Checking whether have Bio content
                self.assertIn(landing_page_content, html_response)
        
                #Chceking whether all About Me Item is rendered
                for item in about_me:
                    self.assertIn(item,html_response)      
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _failed_
    
    >Kali ini kita akan melakukan konsep RED-GREEN-Refactor di Pipeline Gitlab supaya lebih terlihat kesan
    TDD-nya. Yaaay :)
    
1. Buatlah konfigurasi URL di `praktikum/urls.py` untuk `lab_4`
    ```python
        ........
        import lab_4.urls as lab_4
        
        urlpatterns = [
            .....
            url(r'^lab-4/', include(lab_4, namespace='lab-4')),
        ]
    ```
1. Buatlah konfigurasi URL di `lab_4/urls.py`
    ```python
        from django.conf.urls import url
        from .views import index
        
        urlpatterns = [
            url(r'^$', index, name='index'),
         ]
    ```
1. Buatlah sebuah fungsi `index` yang akan meng-_handle_ _Root_ URL dari `lab_4`
    ```python
        from django.shortcuts import render
        from lab_2.views import landing_page_content
        
        # Create your views here.
        response = {'author': ""} #TODO Implement yourname
        about_me = []
        def index(request):
            response['content'] = landing_page_content
            html = 'lab_4/lab_4.html'
            #TODO Implement, isilah dengan 6 kata yang mendeskripsikan anda
            response['about_me'] = about_me
            return render(request, html, response)
    ```
1. Buatlah `base.html` di dalam `lab_4/templates/lab_4/layout` (Jika folder belum tersedia, silahkan membuat folder tersebut)
    ```html
    {% load staticfiles %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="description" content="LAB 4">
        <meta name="author" content="{{author}}">
        <!-- bootstrap csss -->
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">    
    
        <title> 
            {% block title %} Lab 4 By {{author}}{% endblock %}
        </title>
    </head>
    
    <body>
        <header>
            {% include "lab_4/partials/header.html" %}
        </header>
        <content>
            <div class="container">
                {% block content %}
                    <!-- content goes here -->
                {% endblock %}
            </div>
    
        </content>
        <footer>
            <!-- TODO Block Footer dan include footer.html -->
            {% block footer %}
            {% include "lab_4/partials/footer.html" %}
            {% endblock %}
        </footer>
    
        <!-- Jquery n Bootstrap Script -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
    </html>
    ```
1. Buatlah `lab_4.html` di dalam `lab_4/templates/lab_4/`
    ```html
        {% extends "lab_4/layout/base.html" %}
        
        {% block content %}
        <h1>Portofolio</h1>
        <hr/>
        <section name="bio">
            <h2>Bio</h2>
            <p>
                {{content}}
            </p>	
        </section>
        <hr/>
        <section name="about_me">
            <h2>List</h2>
            <ul>
                {% for ii in about_me %}
                <li> {{ ii }} </li>
                {% endfor %}
            </ul>
        </section>
        <hr/>
        {% endblock %}
    ```
1. Buatlah `header.html` di dalam `templates/lab_4/partials`
    ```html
       <!-- Fixed navbar -->
        <nav class="navbar navbar-default navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="{% url 'lab-4:index' %}">Home</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <!-- LINK MENUJU table, dan link menuju home#form -->
                <li><a href="{% url 'lab-4:index' %}#form"> Form </a></li>
                <li><a href="{% url 'lab-4:result_table' %}"> Messages Table </a> </li>
              </ul>
            </div><!--/.nav-collapse -->
          </div>
        </nav>
    ```
1. Buatlah `footer.html` di dalam `templates/lab_4/partials`
    ```html
       <p>&copy; {{author}}</p>
    ```
1. _Copy file_ `lab_4.css` ke dalam `lab_4/static/css/` (Buat _folder_ tersebut jika belum tersedia)
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _passed_  

## Membuat _Form Message_ 

1. Sekarang kita akan membubah sebuah _Form_ isian dengan menggunakan Django _Model Form_. Buatlah _Test_ berikut
di dalam `lab_4/tests.py`
    ```python
        from lab_1.views import mhs_name
        from .models import Message
        from .forms import Message_Form
        # Create your tests here.
        
        class Lab4UnitTest(TestCase):
           .........
            def test_model_can_create_new_message(self):
                #Creating a new activity
                new_activity = Message.objects.create(name=mhs_name,email='test@gmail.com',message='This is a test')
                
                #Retrieving all available activity
                counting_all_available_message= Message.objects.all().count()
                self.assertEqual(counting_all_available_message,1)
            
            def test_form_message_input_has_placeholder_and_css_classes(self):
                form = Message_Form()
                self.assertIn('class="form-control"', form.as_p())
                self.assertIn('<label for="id_name">Nama:</label>', form.as_p())
                self.assertIn('<label for="id_email">Email:</label>', form.as_p())
                self.assertIn('<label for="id_message">Message:</label>', form.as_p())
            
            def test_form_validation_for_blank_items(self):
                form = Message_Form(data={'name': '', 'email': '', 'message': ''})
                self.assertFalse(form.is_valid())
                self.assertEqual(
                    form.errors['message'],
                    ["This field is required."]
                )  
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Buatlah _Models_ untuk `Message` di dalam `lab_4/models.py`
    ```python
        from django.db import models
        
        class Message(models.Model):
            name = models.CharField(max_length=27)
            email = models.EmailField()
            message = models.TextField()
            created_date = models.DateTimeField(auto_now_add=True)
            
            def __str__(self):
                return self.message
    ```
1. Buat file `forms.py` dan masukan kode dibawah
    ```python
    from django import forms

    class Message_Form(forms.Form):
        error_messages = {
            'required': 'Tolong isi input ini',
            'invalid': 'Isi input dengan email',
        }
        attrs = {
            'class': 'form-control'
        }
        
        name = forms.CharField(label='Nama', required=False, max_length=27, empty_value='Anonymous', widget=forms.TextInput(attrs=attrs))
        email = forms.EmailField(required=False, widget=forms.EmailInput(attrs=attrs))
        message = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True)
    ```
1. Test kode secara lokal maka seharusnya sekarang akan _passed_
    
    >Eh ternyata masih _error_ nih, kira - kira kenapa ya Kak PeWe?
    >
    >Ayo ingat - ingat, ketika sudah bikin model baru itu, harus menjnalankan
    _command_ apa :)
1. Sekarang kita akan menampilkan _form_ tersebut dan kita akan membuat fungsi 
untuk memproses data yang di-_submit_ dari _form_ tersebut. Buatlah _test_ berikut
    ```python
        .................
        from .views import index, message_post
     
        class Lab4UnitTest(TestCase):
            ............
            def test_lab4_post_fail(self):
                response = Client().post('/lab-4/add_message', {'name': 'Anonymous', 'email': 'A', 'message': ''})
                self.assertEqual(response.status_code, 302)
        
            def test_lab4_post_success_and_render_the_result(self):
                anonymous = 'Anonymous'
                message = 'HaiHai'
                response = Client().post('/lab-4/add_message', {'name': '', 'email': '', 'message': message})
                self.assertEqual(response.status_code, 200)
                html_response = response.content.decode('utf8')
                self.assertIn(anonymous,html_response)
                self.assertIn(message,html_response)
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Masukan konfigurassi URL berikut pada file `lab_4/urls.py`
    ``` python
        ..........
        from .views import index, add_message
        
        urlpatterns = [
            ...........
            url(r'^add_message', message_post, name='add_message'),
        ]
    ```
1. Masukan template kode berikut pada file `lab_4/views.py`
    ```python
    .............
    from django.http import HttpResponseRedirect
    from .forms import Message_Form
    from .models import Message
    ...............
 
    def index(request):
        ...............
        response['message_form'] = Message_Form
        return render(request, html, response)
    
    def message_post(request):
        form = Message_Form(request.POST or None)
        if(request.method == 'POST' and form.is_valid()):
            response['name'] = request.POST['name'] if request.POST['name'] != "" else "Anonymous"
            response['email'] = request.POST['email'] if request.POST['email'] != "" else "Anonymous"
            response['message'] = request.POST['message']
            message = Message(name=response['name'], email=response['email'],
                              message=response['message'])
            message.save()
            html ='lab_4/form_result.html'
            return render(request, html, response)
        else:        
            return HttpResponseRedirect('/lab-4/')

    ```
1. Ubahlah `lab_4.html` di dalam `lab_4/templates/lab_4/`
    ```html
        ..............
        <section name="form">
            <h2>Send Message</h2>
            <form id="form" method="POST" action="{% url 'lab-4:add_message' %}">
                {% csrf_token %}
                {{ message_form }}
                <br>
                <button type="submit" class="btn btn-default">Submit</button>
            </form>
        </section>
 
        {% endblock %}
    ```
1. Buatlah `form_result.html` di dalam `lab_4/templates/lab_4/`
    ```html

        {% extends "lab_4/layout/base.html" %}
        {% block title %} Pesan dari {{ name }} {% endblock %}
        {% block content %}
        <textarea readonly rows="5" class="form-control">&quot;{{message}}&quot;-{{name}} 
            by {{ email }}
        </textarea>
        {% endblock %}
        
        {% block footer %}
            <p> &copy; {{name}} </p>
        {% endblock %}
 
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _passed_

## Melihat Semua _Message_

1. Kita akan membuat _page_ untuk menampilkan semua _Message_ yang telah diisikan. Tambahkan _test_ berikut
sebelum membuat _page_ tersebut
    ```python
        .......
        from .views import index, message_table, about_me, landing_page_content
        
        
        class Lab4UnitTest(TestCase):
            def test_lab_4_table_url_exist(self):
                response = Client().get('/lab-4/result_table')
                self.assertEqual(response.status_code, 200)
            
            def test_lab_4_table_using_message_table_func(self):
                found = resolve('/lab-4/result_table')
                self.assertEqual(found.func, message_table)
            
            def test_lab_4_showing_all_messages(self):
            
                name_budi = 'Budi'
                email_budi = 'budi@ui.ac.id'
                message_budi = 'Lanjutkan Kawan'
                data_budi = {'name': name_budi, 'email': email_budi, 'message': message_budi}
                post_data_budi = Client().post('/lab-4/add_message', data_budi)
                self.assertEqual(post_data_budi.status_code, 200)
            
                message_anonymous = 'Masih Jelek Nih'
                data_anonymous = {'name': '', 'email': '', 'message': message_anonymous}
                post_data_anonymous = Client().post('/lab-4/add_message', data_anonymous)
                self.assertEqual(post_data_anonymous.status_code, 200)
            
                response = Client().get('/lab-4/result_table')
                html_response = response.content.decode('utf8')
                
                for key,data in data_budi.items():
                    self.assertIn(data,html_response)
                
                self.assertIn('Anonymous', html_response)
                self.assertIn(message_anonymous, html_response
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Tambahkan konfigurasi URL di `lab_4/urls.py`
    ```python
        .........
        from .views import index, message_post, message_table
        
        urlpatterns = [
            .......
            url(r'^result_table', message_table, name='result_table'),
        ]
    ```
1. Tambahkan fungsi berikut kedalam `lab_4/views.py`
    ```python
        ............
        def message_table(request):
            message = Message.objects.all()
            response['message'] = message
            html = 'lab_4/table.html'
            return render(request, html , response)
    ```
1. Ubahlah `table.html` di dalam `lab_4/templates/lab_4/`
    ```html
        {% extends "lab_4/layout/base.html" %}
        
        {% block title %} Kumpulan Pesan {% endblock %}
        
        {% block content %}
        <!--  Populate semua isi pesan dari model -->
        <table class="table">
            <thead>
                <th>Nama</th>
                <th>Email</th>
                <th>Pesan</th>
                <th>Dibuat Pada</th>
            </thead>
            <tbody>
                <!-- TODO, Kalau nama/email anon maka tr classnya jadi warning -->
                {% for i in message %}
                {% if i.name == 'Anonymous' or i.email == 'Anonymous' %}
                <tr class="warning"> {% else %} <tr class="success">
                    {% endif %}
                    <td> {{i.name}} </td>
                    <td> {{i.email}} </td>
                    <td> {{i.message}} </td>
                    <td> {{i.created_date.time}} </td>
                </tr>             
                {% endfor %}
            </tbody>
        </table>
        
        {% endblock %}
        
    ```
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _passed_

## Checklist

1. Membuat _Home Page_
    1. [ ] Buatlah sebuah `app` baru dengan nama `lab-4`
    2. [ ] Buat struktur template pada `app lab-4` seperti dibawah ini
        ```
            - lab_4
                __init__.py
                admin.py
                apps.py
                models.py
                tests.py
                views.py
                - migrations
                    ...
                - templates
                    - layout
                        base.html
                    - partials
                        header.html
                        footer.html
                    table.html
                    lab_4.html
                    from_result.html
        ```
    3. [ ] Isi `navbar.html` dan `footer.html` dengan tag _HTML5_. Pastikan `navbar.html` mengandung tag `<nav>` dan `footer.html` mengandung lambang copyright &copy;
    4. [ ] Isi `base.html` dengan tag _HTML5_ . Buatlah home page yang mendeskripsikan diri kalian. Silahkan berkreasi sesuka hati kalian. Referensi pendukung:
        https://www.html-5-tutorial.com/all-html-tags.htm
        https://www.w3schools.com/TAGs/
    5. [ ] Pada home page terdapat _Form_ untuk memberikan pesan
2. Membuat page Untuk menampilkan semua message
    1. [ ] Terdapat tabel yang menampilkan semua pesan yang telah di-submit
    2. [ ] Pesan dari anonymous diberi warna baris yang berbeda
3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab`
    di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%
4. Additional
    1. [ ] Tampilkan Foto kalian. Gunakan tag `<img>` pada home page dengan bentuk image berbentuk lingkaran
    2. [ ] Berikan tampilan yang menarik pada home page
    3. [ ] Buatlah test baru untuk test keberadaan Navbar dan Copyright
    4. [ ] Tampilkan Pesan error bilamana `Message` diisi kosong (Beserta Testnya)
    5. [ ] Buatlah _custom_ pesan error agar lebih menarik (Beserta Testnya)
    6. [ ] Ubah _Redirection_ ketika mengakses _Root_ URL (`<YOURAPPNAME>.herokuapp.com`) sehingga
    akan mengembalikan halaman _Home Page_ Lab 4 (Kondisikan _Test Case_ dari lab sebelumnya, dan buatlah _Test Case_ baru
    di `lab_4/tests.py` untuk memastikan bahwa _Root URL_ akan mengembalikan halaman _Home Page_ Lab 4)
    7. [ ] Ubah _datetime_ sehingga menggunakan Waktu Lokal GMT + 7