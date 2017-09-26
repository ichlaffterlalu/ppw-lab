# Lab 5: Pengenalan _CSS_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti 

- Mengerti cara penulisan CSS 
- Mengetahui static files dalam django
- Mengerti penggunaan selector pada CSS

## Hasil Akhir Lab
- Membuat halaman TODO List dengan CSS yang sesuai

## Pengenalan CSS

#### Apa itu CSS 

Cascading Style Sheets (CSS) adalah bahasa yang digunakan untuk mendeskripsikan tampilan dan format dari sebuah website yang ditulis pada markup language ( seperti HTML ). Kegunaannya menjadikan tampilan website lebih menarik.

#### Cara penulisan CSS

Secara umum, CSS dapat dituliskan dalam bentuk sebagai berikut.
```css
    selector {
        properties:value;
    }
```

Terdapat 3 jenis cara penulisan CSS

**1. Inline Styles**

Inline styles adalah styles yang didefinisikan langsung pada elemen dan hanya berlaku pada elemen tersebut. Biasa digunakan untuk mengatur tampilan yang bersifat unik pada single element. Definisi dilakukan dengan menambahkan attribute style yang memiliki CSS property dan value yang diinginkan.

```html
	...
	<div id=”main”
		style=”background­-color: #f0f0f0;
		color: red;
		font­-family: georgia;
		font-­size: 0.8em;”>
		...
	</div>
	...
```

Attribute style pada `div` di atas merupakan contoh penulisan inline style. Hal ini akan menyebabkan `div` tersebut akan memiliki properties seperti value yang diberikan.

**2. Internal Style Sheet**

Internal style sheet didefinisikan dalam elemen `style` di dalam elemen `head`. Biasa digunakan jika suatu halaman memiliki style yang unik. Kalian akan mencoba tampilan yang sama seperti pada inline style sebelumnya dengan menggunakan Internal style sheet. Hapus atribut style yang dibuat sebelumnya, kemudian buat element `style` pada elemen head seperti berikut.

```html
	...
	<head>
		...
		<style>
			#main {
				background­-color: #f0f0f0;
				color: red;
				font­-family: georgia;
				font­-size: 0.8em;
			}
		</style>
		...
	</head>
	<body>
		<div id="main">
			...
		</div>
	</body>
	...
```

**3. External Style Sheet**

External style sheet didefinisikan secara terpisah dari dokumen HTML. External style sheet memungkinkan untuk mengubah tampilan lebih dari satu halaman dengan cara memberikan referensi ke satu file css. Untuk mengenal External Style Sheet dapat diikuti tutorial dibawah.

Pertama - tama,  Kalian akan membuat `tutorial.html` yang merujuk pada `tutorial.css` dengan struktur folder seperti berikut.

		lab_5
		├──migrations
		├──templates
			├──lab_5
				├── tutorial.html
		├──static
			├── css
			│   ├── tutorial.css


Kemudian, kalian dapat membuat `tutorial.css` sebagai berikut.

```css
    #main {
        background­-color:#f0f0f0;
        color:red;
        font­-family:georgia;
        font­-size:0.8em;
    }
```

Terakhir, kalian dapat membuat file template HTML kalian merujuk pada file css `tutorial.css`

```html
{% load staticfiles %}
<html>
    <head>
        <title>Tutorial CSS Yay</title>
        <link rel="stylesheet" href="{% static 'css/tutorial.css' %}">
    </head>
    <body>
        <div>
            <h1>Tutorial CSS Yay</h1>
        </div>
        <div id="main">
        	<div>
	            <p>published: 31 September 2017</p>
	            <h1><a href="">Tutorial CSS ku</a></h1>
	            <p>Yay ini tutorial yang gampang!</p>
	         </div>
        </div>
    </body>
</html>
```

Hal ini dapat terjadi karena CSS merupakan `static files` di Django. Tentang `static files` dijelaskan pada bagian selanjutnya.

>Jika terdapat lebih dari satu style yang didefinisikan untuk suatu elemen, maka style yang akan diterapkan adalah yang memiliki prioritas yang lebih tinggi. Berikut ini urutan prioritasnya, nomor 1 yang memiliki prioritas paling tinggi.
>1. Inline style
>2. External dan internal style sheets
>3. Browser default

#### Static files di Django

Pada framework Django, terdapat file - file yang disebut dengan static files. `static files`merupakan file - file pendukung HTML pada suatu website. Contoh `static files` antara lain seperti CSS, Javascript dan gambar. Pengaturan untuk `static files` terdapat dalam `settings.py`

```python
    ...

    # Static files (CSS, JavaScript, Images)
    # httpsdocs.djangoproject.comen1.9howtostatic-files
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
    STATIC_URL = 'static'

    ...
```

Pada `settings.py` terdapat `STATIC_ROOT` yang menentukan _absolute path_ ke direktori `static files` ketika menjalankan perintah `collectstatic` pada project dan terdapat `STATIC_URL` yang merupakan url yang dapat diakses publik untuk memperoleh `static files` tersebut. 

Perintah `collectstatic` adalah perintah untuk mengumpulkan `static files` dari semua `app` sehingga mempermudah akses untuk semua `app`

Lebih lengkap mengenai static files
[static files](httpsdocs.djangoproject.comen1.11howtostatic-files)

## Selector pada CSS

Untuk mempermudah tutorial, kalian dapat tetap menggunakan 'tutorial.html' dan 'tutorial.css'. kalian akan mempelajari 3 buah selector pada CSS, yaitu element selector, class selector, dan id selector 

**1. Element Selector**

Element selector menggunakan tag html sebagai selector untuk mengubah properties yang terdapat dalam tag tersebut. Pada bagian ini, kalian akan menggunakan element selector sebagai berikut pada `tutorial.css`.

```css
    h1 {
        color:#FCA205;
        font-family:'Monospace';
        font-style:italic;
    }
```

Dapat dilihat perubahan tampilan yang terjadi. Properties element `h1` mengalami perubahan.

**2. Id Selector**

Id selector menggunakan id pada tag sebagai selectornya. 

kalian dapat menambahkan id pada template HTML sebagai berikut (id harus bersifat unik).
```html
	...
	<body>
	    <div id="header">
	        <h1>Tutorial CSS Yay</h1>
	    </div>
	...
	</body>
```

Kemudian id tersebut sebagai selector pada 'tutorial.css'.

```css
    #header {
        background-color:#F0F0F0;
        margin-top:0;
        padding:20px 20px 20px 40px;
    }

```

Dapat dilihat perubahan tampilan yang terjadi. Silahkan menambahkan id selector lain untuk mengubah properties.

**3. Class Selector**

Selanjutnya, class selector yang dapat digunakan untuk memperindah tampilan template HTML.

Tambahkan beberapa class pada tag HTML

```HTML
	...
		<div id="main">
			<div class="content_section">
			    <p class="date">published: 31 September 2017</p>
			    <h2><a href="">Tutorial CSS ku</a></h2>
			    <p id="content_1">Yay ini tutorial yang gampang!</p>
			</div>
			<div class="content_section">
			    <p class="date ">published: 32 September 2017</p>
			    <h2><a href="">Tutorial CSS mu</a></h2>
			    <p id="content_2">Yay ini tutorial yang mudah!</p>
			</div>
			<div class="content_section">
			    <p>published: 33 September 2017</p>
			    <h2><a href="">Tutorial CSS semua</a></h2>
			    <p id="content_3">Yay ini tutorial yang tidak sulit!</p>
			</div>
		</div>
	...
```

Kemudian menambahkan class selector pada css

```css
    .content_section {
        background-color:#3696E1;
        margin-bottom: 30px;
        color: #000000;
        font-family: cursive;
        padding: 20px 20px 20px 40px;
    }
```

Dapat dilihat perubahan tampilan yang terjadi. Silahkan menambahkan class selector lain untuk mengubah properties.
 
 > Perbedaan penulisan id selector dan class selector
 > Id Selector menggunakan format #[id_name] selalu diawali #
 > sedangkan class selector menggunakan format .[class_name] diawali . 
 
 Untuk memperdalam pengetahuan mengenai CSS Selector Reference anda dapat membaca info berikut:
 https://www.w3schools.com/cssref/css_selectors.asp
 

## Tips & Tricks CSS

#### Mengenal Combinators

Setelah mengetahui selector pada CSS, kalian dapat mengenal `Combinators` pada CSS. `Combinators` adalah suatu menanda hubungan antar element, class atau id dalam CSS. Terdapat 4 `Combinators` pada CSS :

**1. Descendant selector (space)**

Dengan `Combinators` ini, kalian dapat memilih semua element keturunannya (_descendant_) yang sesuai pola. Contoh sebagai berikut.
    
```html
...
    <div>
        <p>Something here</p>
        <span><p>something special</p></span>
    </div>
    <p> Another thing </p>
    <p> Another thing, again </p>
...
```
    
```css
    div p {
        background-color: red;
    }
```

Dari kode diatas, maka semua tag `p` keturunan tag `div` akan terpilih.

**2. Child selector (>)**

Mirip dengan _descendant selector_, tetapi _child selector_ hanya memilih keturunan pertama _(child)_ dari element yang sesuai pola. 

```css
    div > p {
        background-color: red;
    }
```

Silahkan dicoba, dan lihat perbedaannya.

**3. Adjacent sibling selector (+)**

_Adjacent sibling selector_ hanya memilih satu element dengan level yang setara _(sibling)_ sesuai dengan pola.

```css
    div + p {
        background-color: red;
    }
```

**4. General sibling selector (~)**

Sedangkan _general sibling selector_ akan memilih seluruh _sibling_ yang sesuai dengan pola.

```css
    div ~ p {
        background-color: red;
    }
```

#### Mengenal CSS Pseudo-class

Pseudo-class digunakan untuk mendefinisikan state khusus dari sebuah element. Contoh beberapa pseudo-class 

- :active  memilih elemen yang sedang aktif
- :cheked  memilih elemen yang telah dicentang
- :disabled  memilih elemen yang telah di-nonaktifkan
- :enabled  memilih elemen yang telah di-aktifkan
- :link   memilih link yang belum pernah di kunjungi
- :hover  memilih elemen pada saat mouse berada di atasnya
- :visited  memilih link yang sudah pernah di kunjungi

Umum pseudo-class dituliskan dalam bentuk sebagai berikut.
```css
selector:pseudo-class {
    properties:value;
}
```

#### Perbedaan Margin, Border dan Padding 

<img src="http://1.bp.blogspot.com/-RUtAOT_XsS4/UywVWVG8ohI/AAAAAAAAAL4/HDf0cL0GbGs/s1600/css+margin+padding.gif" alt="margin_padding" width="500" height="300"/>

Dapat dilihat untuk perbedaan margin, border dan padding untuk properties suatu element

#### Pengenalan Bootstrap

Terdapat banyak framework CSS yang sering digunakan sekarang ini, salah satunya adalah Bootstrap CSS. Bootstrap CSS menyediakan class - class yang sering digunakan dalam pengembangan suatu website. Class - class yang disediakan seperti navbar, card, footer, carousel dan lain - lain. Lebih lagi, Bootstrap CSS juga menyediakan banyak fitur yang berguna salah satunya, grid system untuk membagi halaman website menjadi lebih mudah dan menarik.

Lebih lengkap mengenai Bootstrap CSS:
[Bootstrap](httpsgetbootstrap.comdocs3.3csshttpsgetbootstrap.comdocs3.3css)

#### Responsive Web Design

Responsive web design merupakan pendekatan untuk tampilan website tetap terlihat baik pada semua perangkat (baik _desktop_, _tablets_, atau _phones_). Responsive web design tidak mengubah content yang ada, hanya mengubah cara penyajian pada setiap perangkat agar sesuai. Responsive web design menggunakan CSS untuk _resize_, menyusutkan, atau membesarkan suatu element.

 >Content is like water
 >
 >-- Responsive Web Design
 
 Untuk membuka fitur Toggle Device Mode pada browser chrome
 
 Windows/Linux   : `CTRL + SHIFT + M`
 Mac             : `Command + Shift + M`

Lebih lengkap mengenai Reponsive Web Design
[Responsive Web Design](httpsdevelopers.google.comwebfundamentalsdesign-and-uiresponsive)

## Membuat Halaman TODO List

1. Jalankan Virtual Environment kalian
2. _Install tools_ terbaru dari  `requirement.txt`

    >pip install -r requirement.txt
2. Buatlah _apps_ baru bernama `lab_5` 
1. Masukkan `lab_5` kedalam `INSTALLED_APPS`
1. Buatlah _Test_ baru kedalam `lab_5/tests.py` : 
    ```python
        from django.test import TestCase
        from django.test import Client
        from django.urls import resolve
        from .views import index, add_todo
        from .models import Todo
        from .forms import Todo_Form
        
        # Create your tests here.
        class Lab5UnitTest(TestCase):
        
            def test_lab_5_url_is_exist(self):
                response = Client().get('/lab-5/')
                self.assertEqual(response.status_code, 200)
        
            def test_lab5_using_index_func(self):
                found = resolve('/lab-5/')
                self.assertEqual(found.func, index)
        
            def test_model_can_create_new_todo(self):
                # Creating a new activity
                new_activity = Todo.objects.create(title='mengerjakan lab ppw', description='mengerjakan lab_5 ppw')
        
                # Retrieving all available activity
                counting_all_available_todo = Todo.objects.all().count()
                self.assertEqual(counting_all_available_todo, 1)
        
            def test_form_todo_input_has_placeholder_and_css_classes(self):
                form = Todo_Form()
                self.assertIn('class="todo-form-input', form.as_p())
                self.assertIn('id="id_title"', form.as_p())
                self.assertIn('class="todo-form-textarea', form.as_p())
                self.assertIn('id="id_description', form.as_p())
        
            def test_form_validation_for_blank_items(self):
                form = Todo_Form(data={'title': '', 'description': ''})
                self.assertFalse(form.is_valid())
                self.assertEqual(
                    form.errors['description'],
                    ["This field is required."]
                )
            def test_lab5_post_success_and_render_the_result(self):
                test = 'Anonymous'
                response_post = Client().post('/lab-5/add_todo', {'title': test, 'description': test})
                self.assertEqual(response_post.status_code, 302)
        
                response= Client().get('/lab-5/')
                html_response = response.content.decode('utf8')
                self.assertIn(test, html_response)
        
            def test_lab5_post_error_and_render_the_result(self):
                test = 'Anonymous'
                response_post = Client().post('/lab-5/add_todo', {'title': '', 'description': ''})
                self.assertEqual(response_post.status_code, 302)
        
                response= Client().get('/lab-5/')
                html_response = response.content.decode('utf8')
                self.assertNotIn(test, html_response)
    ```
    
1. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
1. Buatlah konfigurasi URL di `praktikum/urls.py` untuk `lab_5`
    ```python
        ........
        import lab_5.urls as lab_5
        
        urlpatterns = [
            .....
            url(r'^lab-5/', include(lab_5, namespace='lab-5')),
        ]
    ```
1. Buatlah konfigurasi URL di `lab_5/urls.py`
    ```python
        from django.conf.urls import url
        from .views import index, add_todo
        
        urlpatterns = [
            url(r'^$', index, name='index'),
            url(r'^add_todo', add_todo, name='add_todo'),
        ]
    ```
1. Buatlah _Models_ untuk `Todo` di dalam `lab_5/models.py`
    ```python
        from django.db import models

        class Todo(models.Model):
            title = models.CharField(max_length=27)
            description = models.TextField()
            created_date = models.DateTimeField(auto_now_add=True)
    ```
1. Jalankan perintah `makemigrations` dan `migrate`
1. Buat file `forms.py` dan masukan kode dibawah
    ```python
    from django import forms

    class Todo_Form(forms.Form):
        error_messages = {
            'required': 'Tolong isi input ini',
        }
        title_attrs = {
            'type': 'text',
            'class': 'todo-form-input',
            'placeholder':'Masukan judul...'
        }
        description_attrs = {
            'type': 'text',
            'cols': 50,
            'rows': 4,
            'class': 'todo-form-textarea',
            'placeholder':'Masukan deskripsi...'
        }

        title = forms.CharField(label='', required=True, max_length=27, widget=forms.TextInput(attrs=title_attrs))
        description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs))
    ```
1. Buatlah fungsi `index` dan `add_todo` yang akan meng-_handle_ URL dari `lab_5`
    ```python
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from .forms import Todo_Form
    from .models import Todo

    # Create your views here.
    response = {}
    def index(request):    
        response['author'] = "" #TODO Implement yourname
        todo = Todo.objects.all()
        response['todo'] = todo
        html = 'lab_5/lab_5.html'
        response['todo_form'] = Todo_Form
        return render(request, html, response)

    def add_todo(request):
        form = Todo_Form(request.POST or None)
        if(request.method == 'POST' and form.is_valid()):
            response['title'] = request.POST['title']
            response['description'] = request.POST['description']
            todo = Todo(title=response['title'],description=response['description'])
            todo.save()
            return HttpResponseRedirect('/lab-5/')
        else:
            return HttpResponseRedirect('/lab-5/')
    ```
1. Buatlah `lab_5.css` di dalam `lab_5/static/css` (Jika folder belum tersedia, silahkan membuat folder tersebut)
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
    section{
      min-height: 600px;
    }
    /* animasi pada title */
    .main-title{
      -webkit-animation: colorchange 1s infinite;
      -webkit-animation-direction: alternate;
      text-align: center;
    }
    
    /* animasi colorchange */
    @-webkit-keyframes colorchange {
        0% {
            -webkit-text-stroke: 5px #0fb8ad;
        letter-spacing: 0;
        }
      50% {
        -webkit-text-stroke: 7.5px  #1fc8db;
      }
        100% {
            -webkit-text-stroke: 10px  #2cb5e8;
        letter-spacing: 18px;
        }
    }
    /* styling wrapper form */
    #input-list{
      background: linear-gradient(to bottom right, #606062, #393939);
    }
    /* styling form */
    #input-list form{
      width: 400px;
      margin: 50px auto;
      text-align: center;
      position: relative;
      z-index: 1;
      background: white;
      border: 0 none;
      border-radius: 3px;
      box-shadow: 0 0 15px 1px rgba(0, 0, 0, 0.4);
      padding: 20px 30px;
      box-sizing: border-box;
      position: relative;
    }
    /* styling judul form, apakah arti dari tanda '>' ? */
    #input-list form > h2{
      font-size: 1.3em;
      text-transform: uppercase;
      color: #2C3E50;
      margin-bottom: 10px;
    }
    /* styling form input dan textarea, apakah arti dari tanda ',' ? */
    #input-list form > .todo-form-input, #input-list form > .todo-form-textarea{
      padding: 15px;
        border: 1px solid #ccc;
        border-radius: 3px;
        margin-bottom: 10px;
        width: 100%;
        box-sizing: border-box;
        color: #2C3E50;
        font-size: 13px;
    }
    /* styling footer */
    footer p{
      text-align: center;
      padding-top: 10px;
    }
    
    /* styling responsive max-width menandakan bahwa rule css ini hanya akan bekerja untuk layar dengan maksimal 768px, jika lebih dari 768px maka rule ini diabaikan */
    @media only screen and (max-width: 768px) {
      #input-list form {
          width: 290px;
      }
    }
    
    #input-list{
      background: linear-gradient(to bottom right, #606062, #393939);
    }
    #input-list form{
      width: 400px;
      margin: 50px auto;
      text-align: center;
      position: relative;
      z-index: 1;
      background: white;
      border: 0 none;
      border-radius: 3px;
      box-shadow: 0 0 15px 1px rgba(0, 0, 0, 0.4);
      padding: 20px 30px;
      box-sizing: border-box;
      position: relative;
    }
    #input-list form > h2{
      font-size: 1.3em;
      text-transform: uppercase;
      color: #2C3E50;
      margin-bottom: 10px;
    }
    #input-list form > .todo-form-input, #input-list form > .todo-form-textarea{
      padding: 15px;
        border: 1px solid #ccc;
        border-radius: 3px;
        margin-bottom: 10px;
        width: 100%;
        box-sizing: border-box;
        color: #2C3E50;
        font-size: 13px;
    }
    
    #my-list{
      background: linear-gradient(141deg, #0fb8ad 0%, #1fc8db 51%, #2cb5e8 75%);
    }
    #my-list .my-list-title{
      font-size: 40px;
      margin-bottom: 1em;
      color: white;
      text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
      text-align: center;
    }
    
    .to-do-list{
      text-align: center;
      background: #fff;
      position: relative;
      z-index: 15;
      margin-bottom: 60px;
      -webkit-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.15);
      -moz-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.15);
      -o-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.15);
      box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.15);
      transition: 0.5s all;
      -webkit-transition: 0.5s all;
      -moz-transition: 0.5s all;
      -o-transition: 0.5s all;
    }
    .to-do-list:after{
        content:"";
        display:block;
        height:25px; /* Which is the padding of div.container */
        background: #fff;
    }
    .flex{
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: flex-start;
      align-items: flex-start;
      align-content: flex-start;
      margin-right: -15px;
      margin-left: -15px;
    }
    .flex-item{
      padding: 0 15px;
      flex-grow: 0;
      flex-shrink: 0;
      flex-basis: 25%;
    }
    
    .to-do-list .to-do-list-title {
      font-size: 20px;
      font-weight: 700;
      padding: 10px 10px 0;
    }
    .to-do-list .to-do-list-date-added {
      font-size: 12px;
      padding: 0 10px;
    }
    .to-do-list .to-do-list-description {
      padding: 10px 25px;
      z-index: 15;
      background: #fff;
      height: 125px;
      text-align: justify;
      overflow: auto;
    }
    .to-do-list .to-do-list-delete {
      background: #e45;
      color: #fff;
      padding: 10px;
      font-size: 16px;
      width: 100%;
      height: 50px;
      bottom: 1px;
      position: absolute;
      cursor: pointer;
      z-index: -1;
      -webkit-border-radius: 0 0px 2px 2px;
      -moz-border-radius: 0 0px 2px 2px;
      -o-border-radius: 0 0px 2px 2px;
      border-radius: 0 0px 2px 2px;
      -webkit-transition: all 0.3s ease;
      -moz-transition: all 0.3s ease;
      -o-transition: all 0.3s ease;
      transition: all 0.3s ease;
    }
    .to-do-list .to-do-list-delete {
      bottom: -50px;
    }

    ```
1. Buatlah `base.html` di dalam `lab_5/templates/lab_5/layout` (Jika folder belum tersedia, silahkan membuat folder tersebut)
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
        

        <title>
            {% block title %} Lab 5 By {{author}} {% endblock %}
        </title>
    </head>

    <body>
        <header>
            {% include "lab_5/partials/header.html" %}
        </header>
        <content>
                {% block content %}
                    <!-- content goes here -->
                {% endblock %}
        </content>
        <footer>
            <!-- TODO Block Footer dan include footer.html -->
            {% block footer %}
            {% include "lab_5/partials/footer.html" %}
            {% endblock %}
        </footer>

        <!-- Jquery n Bootstrap Script -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script type="application/javascript">
          $(function() {
              $('a[href*="#"]:not([href="#"])').click(function() {
                if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
                  var target = $(this.hash);
                  target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                  if (target.length) {
                    $('html, body').animate({
                      scrollTop: target.offset().top - 55
                    }, 1000);
                    return false;
                  }
                }
              });
            });
        </script>
    </body>
    </html>
    ```
1. Agar bisa mengakses _bootstrap_ serta _css_ yang sudah kalian buat, tambahkan link ke `lab_5.css` pada `base.html`
    ```html
    <head>
    ...
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="{% static 'css/lab_5.css' %}" />
    ...
    </head>
    ```
1.  Buatlah `header.html` dan `footer.html` pada folder `templates/lab_5/partials`

    ```html
    <!-- templates/lab_5/partials/header.html -->
    <nav>
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="">Home</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <!-- LINK MENUJU table, dan link menuju home#form -->
            <li><a href="{% url 'lab-5:index' %}#input-list">Input Todo</a></li>
            <li><a href="{% url 'lab-5:index' %}#my-list">My List</a> </li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    ...
    ```
    ```html
    <!-- templates/lab_5/partials/footer.html -->
    <!-- TODO, CREATE THIS FILE AND ADD copyright symbol -->
    <p>Made with Love by {{author}}</p>

    ```
1. Buatlah `lab_5.html` di dalam `lab_5/templates/lab_5/`
    ```html
    {% extends "lab_5/layout/base.html" %}

    {% block content %}
    <h1 class="main-title">TODOLIST</h1>
    <hr/>
    <section name="input-list" id="input-list">
        <div class="container">
            <form id="form" method="POST" action="{% url 'lab-5:add_todo' %}">
                <h2>Input Todo</h2>
                {% csrf_token %}
                {{ todo_form }}
                <input id="submit" type="submit" class="btn btn-lg btn-block btn-info" value="Submit">
                <br>
            </form>
        </div>
    </section>
    <section name="my-list" id="my-list">
        <div class="container">
            <h2 class="my-list-title">My List</h2>
            <div class="flex">
                {% if todo %}
                    {% for data in todo %}
                        <div class="flex-item">
                            <div class="to-do-list">
                                <div class="to-do-list-title">
                                    {{data.title}}
                                </div>
                                <div class="to-do-list-date-added">
                                    {{data.created_date}}
                                </div>
                                <div class="to-do-list-description">
                                    {{data.description}}
                                </div>
                                <div class="to-do-list-delete">
                                    <div class="to-do-list-delete-button" data-id="{{data.id}}">Delete</div>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                {% else %}
                <div class="alert alert-danger text-center">
                    <strong>Oops!</strong> Tidak ada data Todo.
                </div>
                {% endif %}
            </div>
        </div>
    </section>


    {% endblock %}        
    ```
1. Aturlah `static file` agar dapat di deploy pada heroku. 
    1. Install whitenoise dengan perintah berikut.
        > pipenv install whitenoise
    2. Pada `settings.py` pastikan pengaturan middleware dan storagenya seperti berikut ini.
        ```python
        MIDDLEWARE_CLASSES = (
            # Simplified static file serving.
            # https://warehouse.python.org/project/whitenoise/
            'whitenoise.middleware.WhiteNoiseMiddleware',
            ...
        ```
        ```python
            ...
            # Simplified static file serving.
            # https://warehouse.python.org/project/whitenoise/

            STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        ```
    3. Pada proses build, heroku akan secara otomatis menjalankan ` python manage.py collectstatic --noinput`. Jika terjadi kegagalan pada proses build maka jalankan `heroku config:set DEBUG_COLLECTSTATIC=1` untuk mengetahui kesalahan yang terjadi.
    4. Jika masih kesulitan dalam proses deploy, dapat mengunjungi link ini. [Help Deploy Heroku](https://devcenter.heroku.com/articles/django-assets)

1. _Commit_ dan _push_. Kemudian, lanjutkan pada bagian testing.

## Melakukan Testing menggunakan Selenium

#### Testing dengan selenium pada local environment

1.  Buat `class` baru `tests.py` sebagai berikut.

    ```python
    .............
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    
    
    
    # Create your tests here.
    class Lab5FunctionalTest(TestCase):
    
        def setUp(self):
            chrome_options = Options()
            self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
            super(Lab5FunctionalTest, self).setUp()
    
        def tearDown(self):
            self.selenium.quit()
            super(Lab5FunctionalTest, self).tearDown()
    
        def test_input_todo(self):
            selenium = self.selenium
            # Opening the link we want to test
            selenium.get('http://127.0.0.1:8000/lab-5/')
            # find the form element
            title = selenium.find_element_by_id('id_title')
            description = selenium.find_element_by_id('id_description')
    
            submit = selenium.find_element_by_id('submit')
    
            # Fill the form with data
            title.send_keys('Mengerjakan Lab PPW')
            description.send_keys('Lab kali ini membahas tentang CSS dengan penggunaan Selenium untuk Test nya')
    
            # submitting the form
            submit.send_keys(Keys.RETURN)
    ```
2.  Dapat dilihat pada `tests.py` terdapat import library `selenium`
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    ...
    ```
2. Install `selenium` dengan command:
    > pip install selenium

3. Download `chromedriver` sesuai dengan OS kalian pada url berikut.
[Download chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=2.32/)

4. `unzip` chromedriver pada folder project kalian. (Akan menghasilkan `chromedriver.exe` pada Windows dan `chromedriver` pada Linux dan Mac). Berikut struktur folder (contoh pada windows)

            lab-ppw
    		├──lab_1
    		├──lab_2
    		├──...
            ├──lab_5
            ├── manage.py
            ├──...
            ├── README.md
            ├── chromedriver.exe
            ├──...

5. Mengatur `tests.py` seperti berikut. (contoh pada windows)
    ```python
    ...
    def setUp(self):
        chrome_options = Options()
        self.selenium  = webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)
        super(Lab5UnitTest, self).setUp()
    ...
    ```

6. Pastikan kalian memiliki chrome browser.
7. Jalankan `./manage.py collectstatic`
7. Jalankan `./manage.py runserver`
8. Buka terminal baru, jalankan test dengan `./manage.py test`
9. Lihat chrome browser akan terbuka dan melakukan test secara otomatis.

#### Testing dengan selenium dengan gitlab-ci

1. Pastikan kalian telah melakukan **Testing dengan selenium pada local environment** langkah 1 hingga 4.

2. Mengatur `tests.py` seperti berikut.
    ```python
    ...
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--dns-prefetch-disable')
        chrome_options.add_argument('--no-sandbox')        
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')
        self.selenium  = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
        super(Lab5UnitTest, self).setUp()
    ...
    ```

3. Pastikan file `.gitignore` pada baris terakhir memiliki ini.

    ```bash
    ...
    #ignore chromedriver
    chromedriver
    chromedriver.exe
    /pratikum/static/*
    ```
4. _Commit_ dan _push_.

Penjelasan mengenai selenium :
[Click me](http://www.seleniumhq.org/)

## Checklist

1.  Membuat CSS yang sesuai untuk halaman TODO List
    1. [ ] Tambahkan class bootstrap pada navbar, agar navbar static diatas.
    2. [ ] Load object `Todo` pada `views.py` kemudian masukan kedalam response.
    3. [ ] Buatlah tag section dengan `id=‘my-list’` pada lab_5.html.
    4. [ ] Buatlah sebuah tag div dengan `class=‘flex’` didalam section my-list.
    5. [ ] Buatlah child div dengan `class=‘flex-item’` dari flex.
    6. [ ] Lakukan looping data `todo` yang sudah di load pada `views.py` kedalam flex-item. Data `TODO List` yang akan dirender pada flex-item harus memiliki title, created_date dan description.
    7. [ ] Tambahkan rule css untuk div yang telah dibuat menggunakan display flex, implementasikan sendiri. **Dilarang menggunakan css framework untuk flex.** Berikut adalah guide yang mungkin akan membantu.
    https://css-tricks.com/snippets/css/a-guide-to-flexbox/
    8. [ ] Untuk tampilan desktop >= 768 px susun agar terdapat empat flex-item dalam satu baris, jika lebih maka akan dipindahkan ke baris selanjutnya.
    [ScreenShot 1](https://drive.google.com/file/d/0BzEo5TOpZj0VSXIyVTN1NkZHTXc/view?usp=sharing)
    9. [ ] Untuk tampilan mobile < 768 px hanya terdapat satu flex-item pada setiap baris.
    [ScreenShot 2](https://drive.google.com/file/d/0BzEo5TOpZj0VcDNTTXFkb0hwblU/view?usp=sharing)
    10. [ ] Pastikan rule css yang telah dibuat responsive untuk ukuran mobile, dibawah 768px. Gunakan fitur Toggle Device Mode pada browser.
    
2.  Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ]  Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md).
    2. [ ] Pastikan _Code Coverage_ kalian 100%.

###  Challenge Checklist
Cukup kerjakan salah satu nya saja:
1.  [ ] Tambahkan efek `box-shadow` dan animasi bergerak keatas sejauh `5px` pada setiap flex-item ketika di `hover`.
2.  [ ] Implementasikan fungsi delete `todo` untuk menghapus `todo` yang sudah dibuat dengan menekan sebuah button pada  setiap flex-item.
3.  [ ] Tambahkan efek `hover` untuk _button delete_, sehingga _button delete_ hanya akan tampil ketika salah satu `to do` di `hover`.
4.  [ ] Buatlah _Functional Test_ dan _Unit Test_ untuk melakukan _Testing_ tombol `delete`. 
5.  [ ] Masukkan kode berikut kedalam `lab_5/tests.py` class `Lab5FunctionalTest` method `test_input_todo`
, lalu _solve_ Test `test_input_todo` yang sudah ditambahkan kode berikut :
    
    ```python
        # check the returned result
            assert 'Berhasil menambahkan Todo' in selenium.page_source
<<<<<<< HEAD
    ```

### Additional Info

Untuk implementasi lengkap semua _Checklist_ bisa dilihat di [sini](https://igun-lab.herokuapp.com/lab-5/)

Credit by [@EdisonTantra](https://gitlab.com/EdisonTantra), [@falsewaly](https://gitlab.com/falsewaly), 
[@fajrinajiseno](https://gitlab.com/fajrinajiseno), and [@glory.finesse](https://gitlab.com/glory.finesse).

Verified by [@hafiyyan94](https://gitlab.com/hafiyyan94) and [@KennyDharmawan](https://gitlab.com/KennyDharmawan)
=======
    ```
>>>>>>> f1756ed5c1035108ef18d7d4cf4783ebd1b5757a
