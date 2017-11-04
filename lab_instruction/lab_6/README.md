# Lab 6: Pengenalan _Javascript dan JQuery_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti

- Pengenalan Javascript
- Pengenalan fungsi Javascript pada front-end development
- Penggunaan dasar javascript
- Perkembangan teknologi javascript

## Hasil Akhir Lab
- Membuat calculator dengan JavaScript
- Membuat chatbox dengan JavaScript
- Membuat fitur mengganti tema dengan select2

## Pengenalan Javascript

#### Apa itu Javascript

JavaScript merupakan bahasa pemrograman multi-paradigma tingkat tinggi lintas
platform (cross platform high-level multi-paradigm programming language). Sifat
multi-paradigma membuat JavaScript mendukung konsep object-oriented programming, imperative programming, dan functional programming. JavaScript sendiri merupakan
implementasi dari ECMAScript, yang merupakan core dari bahasa JavaScript. Beberapa
implementasi lain dari ECMAScript yang mirip dengan JavaScript antara lain JScript (Microsoft)
dan ActionScript (Adobe).


JavaScript, bersama dengan HTML dan CSS, menjadi 3 teknologi utama yang dipakai
pada pengembangan web. Keuntungan menggunakan JavaScript dalam pengembangan
web, pada dasarnya, antara lain JavaScript dapat memanipulasi halaman web secara
dinamis dan memberikan interaksi lebih kepada pengguna. Oleh karena itu, hampir semua
website modern saat ini menggunakan JavaScript dalam halaman web mereka untuk memberikan
pengalaman terbaik kepada pengguna. Beberapa contoh hal yang dapat kita lakukan dengan
menggunakan JavaScript antara lain menampilkan informasi berdasarkan waktu, mengenali jenis
browser pengguna, melakukan validasi form atau data, membuat cookies (bukan kue, tapi
[cookies](https://en.wikipedia.org/wiki/HTTP_cookie)), mengganti styling dan CSS suatu element secara dinamis, dan lain­lain.
Pada pengembangan web umumnya kode JavaScript digunakan pada client-side suatu
web (Client­side JavaScript) namun beberapa jenis kode JavaScript saat ini digunakan pada
server­side suatu web (Server­side JavaScript) seperti node.js. Istilah Client-side menunjukkan
bahwa kode JavaScript akan dieksekusi atau dijalankan pada browser pengguna, bukan pada
server website. Hal ini berarti kompleksitas kode JavaScript tidak akan mempengaruhi performa
server website tersebut namun mempengaruhi performa browser dan komputer, semakin
kompleks kode JavaScript semakin banyak memori komputer yang dikonsumsi oleh browser.

Pada mata kuliah PPW ini kita hanya akan fokus pada kode client-side JavaScript.

#### Bagaimana tahapan JavaScript dieksekusi oleh browser?

Perhatikan diagram berikut.

![javascript-works](https://preview.ibb.co/e258TG/Screenshot_from_2017_10_31_14_29_13.png)

Setelah browser mengunduh halaman HTML web maka tepat dimana tag <script></script>
berada, browser akan melihat tag script tersebut, apakah tag tersebut berisi kode embedded
JavaScript atau merujuk file external JavaScript. Jika merujuk pada file external JavaScript maka
browser akan mengunduh file tersebut terlebih dahulu.

__Cara penulisan Javascript__

Cara penulisan JavaScript bisa dilakukan dengan __embedded javascript__ atau __external javascript__.
Kode JavaScript dapat didefinisikan atau dituliskan secara embedded pada file HTML maupun
secara terpisah pada file tersendiri. Jika ditulis dalam file terpisah dari HTML, ekstensi file yang
digunakan untuk file JavaScript adalah .js. Berikut contoh beberapa pendefinisian dan JavaScript.

JavaScript dapat di letakkan pada head atau body dari HTML page. Selain itu, kode JavaScript
__HARUS__ dimasukkan di antara tag ```<script>``` dan ```</script>```. Anda dapat meletakkan lebih dari satu
tag script yang berisi JavaScript pada suatu file HTML.

__Embedded JavaScript pada HTML__

index.html
```html
<script type="text/JavaScript">
    alert("Hello World!");
</script>
```

__External JavaScript pada HTML__

index.html
```html
<script type="text/JavaScript" src="js/script.js"></script>
```
js/script.js
```javascript
alert("Hello World!")
```
Pada file external JavaScript tidak perlu lagi menambahkan tag ```<script>```.
Memisahkan JavaScript pada file tersendiri memberikan beberapa keuntungan seperti kode dapat
digunakan di file HTML lain, kode JavaScript dan HTML tidak bercampur sehingga lebih fokus,
mempercepat loading halaman. File .js biasanya akan di cache oleh browser sehingga jika kita load page yang sama dan tidak ada perubahan pada file .js maka browser tidak akan request file .js tersebut ke server lagi, akan menggunakan file dari cache yang sudah disimpan sebelumnya.

#### Eksekusi JavaScript

Kemudian setelah JavaScript sudah terunduh dengan sempurna maka browser akan langsung
mulai mengeksekusi kode JavaScript. Jika kode tersebut BUKAN merupakan event triggered
maka kode langsung dieksekusi. Jika kode tersebut merupakan event triggered maka kode
tersebut hanya akan dieksekusi jika event yang didefinisikan triggered.

```javascript
// langsung dieksekusi
alert("Hello World");

// langsung dieksekusi
var obj = document.getElementById("object");
// langsung dieksekusi, menambahkan event handler onclick untuk element object
obj.onclick = function() {
    // hanya dieksekusi jika element 'object' di klik
    alert("You just click the object!");
};
```

#### Syntax JavaScript

__Variable__

Mendefinisikan variabel pada JavaScript cukup mudah. Contohnya seperti

```javascript
    var contoh = 0;     // var contoh merupakan sebuah bilangan
    var contoh = "contoh";// var contoh merupakan sebuah string
    var contoh = true;  // var contoh merupakan sebuah boolean
```

Javascript dapat menampung banyak jenis data, mulai string, integer hingga object sekalipun.
Berbeda dengan Java, yang penandaan jenis data dibedakan dengan head variable (contoh ingin
membuat variable int, int x = 9), JavaScript mempunyai ciri khas loosely typed or a dynamic
language, yakni kalian tidak perlu menuliskan jenis data pada head variable, dan JavaScript
nantinya akan secara otomatis membaca jenis data kalian berdasarkan standar yang ada. Seperti
pada contoh diatas. Untuk lebih jelasnya kalian bisa baca pada link ​ini​.

Ada beberapa aturan dalam pemilihan indentifiers atau nama variable dalam JavaScript. Karakter
pertama HARUS ​merupakan alphabet, underscore ( _ ), atau karakter dollar ($). ​Selain itu
JavaScript identifiers bersifat case sensitive.

__Aritmatika__

Javascript juga dapat melakukan operasi aritmatika, contoh dibawah ini adalahkalkulator 
sederhana dengan menggunakan HTML DOM (DOM akan dijelaskan di bawah).

Kode index.html

```javascript
...
<form>
    <h3>Kalkulator Penambahan </h3>
    Angka Pertama: <input type="text" id="number1" />
    Angka Kedua: <input type="text" id="number2" />
    <input type="button" name="submit" value="Submit" onclick="tambahkan();" />
    <p id ="hasil"></p>
</form>
...
```
Kode javascript.js

```javascript
function tambahkan() {
    var x = parseInt(document.getElementById("number1").value);
    var y = parseInt(document.getElementById("number2").value);
    var z = x+y;
    document.getElementById("hasil").innerHTML = z;
}
```

__String Concatenation__

Dalam JavaScript, kita juga dapat menyambungkan string dengan string lainnya seperti pada
Java.

```javascript
var str1 = "PPW"+" "+"Asik";
var str2 = "PPW";
var str3 = "Asik";
var str4 = str2+" "+str3;
```

#### Javascript Scope

__Local Variable__

Variable yang didefinisikan dalam function hanya dapat diakses oleh kode didalam fungsi
tersebut, bersifat lokal

```javascript
// kode diluar fungsi iniFungsi() tidak dapat mengakses variable namaMatkul
function iniFungsi() {
    var namaMatkul = "PPW";
    // kode di dalam fungsi ini dapat mengakses variable namaMatkul
}
```

__Global Variable__

Variable yang didefinisikan DI LUAR ​function bersifat global dan dapat diakses oleh kode lain
dalam file JavaScript tersebut

```javascript
var namaMatkul = "PPW";
function iniFungsi() {
    // kode di dalam fungsi ini dapat mengakses variable namaMatkul
}
```

__Auto Global Variable__

Value yang di­assign pada variable yang belum dideklarasikan otomatis menjadi global variable
walaupun variable tersebut berada di dalam suatu function.

```javascript
iniFungsi(); // function iniFungsi() perlu dipanggil terlebih dahulu
console.log(namaMatkul); // print "PPW" pada JavaScript console
function iniFungsi() {
    namaMatkul = "PPW";
}
```

__Mengakses Global Variable dari HTML__

Anda dapat mengakses global variable ​yang berada dalam file JavaScript pada file HTML yang
mengunduh file JavaScript tersebut

```html
...
<input type="text"
onclick="this.value=namaMatkul"/>
...
```

```javascript
...
var namaMatkul = "PPW";
...
```

#### Function dan Event

Function adalah grup­grup dari kode­kode yang bisa dipanggil dimanapun pada bagian
kode program (mirip dengan method java). Hal ini mengurangi redundansi untuk mengurangi
kode­kode yang dapat sama berulang­ulang. Selain itu, function pada JavaScript sangat berguna
untuk memudahkan elemen pemanggilan secara dinamis. Function dapat dipanggil sesama
function dan dapat juga dipanggil karena event (akan dijelaskan di bawah). Sebagai contoh,
berikut kode yang terdapat pada index.html

```html
...
<input type="button" value="magicButton" id="magicButton" onclick="hore();" />
...
```

kemudian berikut adalah kode pada javascript.js

```javascript
...
function hore(){
    alert("Hati­hati tugas 1 PPW berbahaya!");
}
...
```

Sehingga apabila magicButton ditekan maka dengan fungsi onclick akan menjalankan function hore() pada javascript.js,
lalu muncul alert sesuai yang sudah diassign disitu.

Kode onclick sebenarnya adalah salah satu contoh kemampuan JavaScript yang disebut
event. Event adalah kemampuan JavaScript untuk membuat sebuah website dinamis. Maksud
dari onclick adalah penanda apa yang akan dilakukan JavaScript jika elemen tersebut ditekan.
Lebih jauh, event biasanya diberikan sebuah function yang berguna sebagai command­command
untuk JavaScript. Selain itu, banyak contoh­contoh event lainnya seperti : onchange,
onmouseover, onmouseout dan lain sebagainya yang bisa kalian baca pada link
[ini](https://www.tutorialspoint.com/javascript/javascript_events.html)

#### Javasciprt HTML & CSS DOM

__HTML DOM__

HTML DOM (Document Object Model) adalah standar bagaimana mengubah,
mengambil, menghapus HTML elements. HTML DOM dapat diakses melalui JavaScript atau
dengan bahasa pemrograman lainnya. Dengan lengkapnya dapat dilihat 
[disini](https://www.w3schools.com/js/js_htmldom.asp)

Berikut contoh implementasinya :

```html
...
    <div>
        <p onclick="myFunction()" id="demo" >Ini Percobaan HTML DOM</p>
    </div>
...
```

```javascript
...
    function myFunction() {
document.getElementById("demo").innerHTML = "YOU CLICKED ME!";
    }
...
```

__CSS DOM__

Sama dengan HTML DOM, DOM CSS dapat mengubah CSS secara dinamis melalui
JavaScript. Lebih lengkapnya terdapat [disini](https://www.w3schools.com/js/js_htmldom_css.asp) 
Berikut ini adalah contohnya :

index.html

```html
...
<p id="textBiru" onclick="gantiWarna()">Click me v2</p>
...
```

javascript.js
```javascript
...
function gantiWarna(){
    document.getElementById("textBiru").style.color="blue";
}
...
```

## Web Storage

Dengan penyimpanan lokal, aplikasi web dapat menyimpan data secara lokal dalam browser pengguna.
Sebelum HTML5, data aplikasi harus disimpan dalam cookies , termasuk dalam setiap permintaan server. penyimpanan lokal lebih aman, dan sejumlah besar data dapat disimpan secara lokal, tanpa mempengaruhi kinerja website.
Tidak seperti cookies , batas penyimpanan jauh lebih besar (at least 5MB) dan informasi yang tidak pernah ditransfer ke server.
Penyimpanan lokal adalah per asal (per domain and protocol) . Semua halaman, dari satu asal, dapat menyimpan dan mengakses data yang sama.

Terdapat 2 cara menyimpan data menggunakan web storage. Yaitu :
    - window.localStorage - menyimpan data tanpa tanggal kadaluarsa
    - window.sessionStorage - menyimpan data untuk satu session (data hilang ketika tab browser ditutup)

__localStorage Object__

Objek localStorage menyimpan data tanpa tanggal kedaluwarsa. Data tidak akan dihapus ketika browser ditutup, dan akan tersedia pada hari berikutnya, minggu, atau tahun.

Berikut contoh implementasinya :

index.html
```html
...
<p><button onclick="clickCounter()" type="button">Click me!</button></p>
<div id="result"></div>
<p>Click the button to see the counter increase.</p>
<p>Close the browser tab (or window), and try again, and the counter will continue to count (is not reset).</p>
...
```

```javascript
...
function clickCounter() {
    if(typeof(Storage) !== "undefined") {
        if (localStorage.clickcount) {
            localStorage.clickcount = Number(localStorage.clickcount)+1;
        } else {
            localStorage.clickcount = 1;
        }
        document.getElementById("result").innerHTML = "You have clicked the button " + localStorage.clickcount + " time(s).";
    } else {
        document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
    }
}
...
```

Apabila dijalankan program tersebut, ketika tombol di click maka terhitung jumlah click akan bertambah.
Ketika browser di close, dan kita membuka kembali, dapat dilihat bahwa perhitungan jumlah click
akan dilanjutkan dari yang sebelumnya.

__sessionStorage Object__

Sama dengan yang atas cuma diganti menggunakan sessionStorage. Yang terjadi adalah apabila browser di close
dan membuka lagi page tersebut, click count akan kembali menjadi 0.

Berikut lebih lengkapanya untuk 
[HTML5 WebStorage](http://www.w3im.com/id/html/html5_webstorage.html)


## Pengenalan jQuery

Selain itu ada library JavaScript yang cukup terkenal, yakni jQuery. Seperti slogannya
yakni, The Write Less, Do More, jQuery membuat kode dari JavaScript menjadi sangat singkat
dari pada sebelumnya. JQuery dibuat oleh John Resign pada tahun 2006. Beberapa kode
JavaScript seperti document traversing, event handling, animating, dan AJAX dapat didukung
oleh jQuery dengan akses sangat mudah. Instalasi jQuery dapat menggunakan 2 cara, yakni
mendownload jQuery dari jQuery.com atau diakses melalui CDN. Pada tutorial kali ini, kita
akan mencoba menggunakan jQuery (menggunakan CDN) dalam mengerjakan soal yang ada.

Pada tutorial kali ini kita akan menggunakan external JavaScript dan jQuery, oleh karena itu
buatlah file __lab_6.js__ dari text editor Anda pada folder lab_6/static/js.

```javascript
$(document).ready(function(){
    // kode jQuery selanjutnya akan ditulis disini
});
```

## Static files di Django

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

#### Membuat Chat Box Sederhana
1. Buatlah `lab_6.css` di dalam `lab_6/static/css` (Jika folder belum tersedia, silahkan membuat folder tersebut)
    ```css
        *{
          padding: 0px;
          margin: 0px;
          font-family: 'Fira Code';
        }
        body{
          height: 100%;
          background: #95a5a6;
        }
        .chat-box{
          position: absolute;
          right: 20px;
          bottom: 0px;
          background: white;
          width: 300px;
          border-radius: 5px 5px 0px 0px;
        }
        .chat-head{
          width: inherit;
          height: 100%;
          background: #2c3e50;
          border-radius: 5px 5px 0px 0px;
        }
        .chat-head h2{
          color: white;
          padding: 8px;
          display: inline-block;
        }
        .chat-head img{
          cursor: pointer;
          float: right;
          width: 25px;
          margin: 10px;
        }
        .chat-body{
          height: 355px;
          width: inherit;
          overflow: auto;
          margin-bottom: 45px;
        }
        .chat-text{
          position: fixed;
          bottom: 0px;
          height: 45px;
          width: inherit;
        }
        .chat-text textarea{
          width: inherit;
          height: inherit;
          box-sizing: border-box;
          border: 1px solid #bdc3c7;
          padding: 10px;
          resize: none;
        }
        .chat-text textarea:active, .chat-text textarea:focus, .chat-text textarea:hover{
          border-color: royalblue;
        }
        .msg-send{
          background: #2ecc71;
        }
        .msg-receive{
          background: #3498db;
        }
        .msg-send, .msg-receive{
          width: 200px;
          height: 35px;
          padding: 5px 5px 5px 10px;
          margin: 10px auto;
          border-radius: 3px;
          line-height: 30px;
          position: relative;
          color: white;
        }
        .msg-receive:before{
          content: '';
          width: 0px;
          height: 0px;
          position: absolute;
          border: 15px solid;
          border-color: transparent #3498db transparent transparent;
          left: -29px;
          top: 7px;
        }
        .msg-send:after{
          content: '';
          width: 0px;
          height: 0px;
          position: absolute;
          border: 15px solid;
          border-color: transparent transparent transparent #2ecc71;
          right: -29px;
          top: 2.5px;
        }
        .msg-receive:hover, .msg-send:hover{
          opacity: .9;
        }
    ```

2. Buatlah `base.html` di dalam `lab_6/templates/lab_6/layout` (Jika folder belum tersedia, silahkan membuat folder tersebut)
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
        <link rel="stylesheet" type="text/css" href="{% static 'css/lab_6.css' %}" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Droid+Sans:400,700">
        <title>
            {% block title %} Lab 6 By {{author}} {% endblock %}
        </title>
    </head>
    <body>
        <header>
            {% include "lab_6/partials/header.html" %}
        </header>
        <content>
                {% block content %}
                    <!-- content goes here -->
                {% endblock %}
        </content>
        <footer>
            <!-- TODO Block Footer dan include footer.html -->
            {% block footer %}
            {% include "lab_6/partials/footer.html" %}
            {% endblock %}
        </footer>
        <!-- Jquery n Bootstrap Script -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </body>
    ```
3. Agar bisa mengakses _script_  yang sudah kalian buat, tambahkan link ke `lab_6.js` pada `base.html`
    ```html
        ...
        <!-- Jquery n Bootstrap Script -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script type="application/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="{% static 'js/lab_6.js' %}"></script>
        ...
    ```

4. Buatlah `lab_6.html` di dalam `lab_6/templates/lab_6/`
    ```html
    {% extends "lab_6/layout/base.html" %}

    {% block content %}
        <!-- ChatBox Section -->
        <section name="Chatbox">
           <div class="wrapper">
              <div class="chat-box">
                 <div class="chat-head">
                    <h2>Chat</h2>
                    <img src="https://maxcdn.icons8.com/windows10/PNG/16/Arrows/angle_down-16.png" title="Expand Arrow" width="16">
                 </div>
                 <div class="chat-body">
                    <div class="msg-insert">
                    </div>
                    <div class="chat-text">
                       <textarea placeholder="Press Enter"></textarea>
                    </div>
                 </div>
              </div>
           </div>
        </section>
        {% endblock %}
    ```

5. Buatlah `lab_6.js` di dalam `lab_6/static/js` (Jika folder belum tersedia, silahkan membuat folder tersebut)
6. Lengkapi kode pada file __lab_6.js__ agar potongan kode dapat berjalan

7. Aturlah `static file` agar dapat di deploy pada heroku.
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

8. _Commit_ dan _push_.

#### Membuat Calculator
1. Tambahkan kode di bawah ke dalam file `lab_6.css` yang telah dibuat sebelumnya.
    ```css
    ...

    .calculator {
      margin-top: 15%;
      margin-bottom: 15%
    }

    .calculator .model {
      background: #4e4e4e;
    }
    .calculator .calcs {
      font-size: 56px;
      padding-top: 15px;
      padding-bottom: 15px;
      height: auto;
      border-radius: 0;
      cursor: text;
    }

    .calculator #title {
      color: #f9f9f9;
    }

    .calculator .btn {
      border-radius: 0;
    }

    ...
    ```
2. Tambahkan kode di bawah ke dalam file `base.html` di dalam `lab_6/templates/lab_6/layout` (Jika folder atau file belum tersedia, pastikan anda telah mengikuti langkah sebelumnya)
    ```html
    ...

      <!-- Calculator Section -->
      <section class="calculator">
        <div class="container">
            <div class="model col-lg-5">
                <div class="container-fluid">
                    <div class="row" id="title">
                        <h1 class="text-center">
                            CALCULATOR
                        </h1>
                    </div>
                    <div class="row" id="calcs-section">
                        <div class="row">
                            <input id="print" type="text" readonly="readonly" class="form-control text-right calcs" id="usr">
                        </div>
                    </div>
                    <!-- Adapted from Tom Howard -->
                    <div class="row" id="calc-buttons">
                        <div class="row">
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go('ac');">AC</button>
                            <!-- <button class="btn btn-lg btn-default col-xs-3" onClick="go('log');">log</button> -->
                            <!-- <button class="btn btn-lg btn-default col-xs-3" onClick="go('sin');">sin</button> -->
                            <!-- <button class="btn btn-lg btn-default col-xs-3" onClick="go('tan');">tan</button> -->
                        </div>
                        <div class="row">
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(7);">7</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(8);">8</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(9);">9</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(' * ');">*</button>
                        </div>
                        <div class="row">
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(4);">4</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(5);">5</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(6);">6</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(' - ');">-</button>
                        </div>
                        <div class="row">
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(1);">1</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(2);">2</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(3);">3</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(' + ');">+</button>
                        </div>
                        <div class="row">
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(0);">0</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go('.');">.</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go('eval');">=</button>
                            <button class="btn btn-lg btn-default col-xs-3" onClick="go(' / ');">/</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    ...
    ```
3. Tambahkan kode di bawah ke dalam file `lab_6.js` di dalam `lab_6/static/js` (Jika folder atau file belum tersedia, pastikan anda telah mengikuti langkah sebelumnya). Lakukan penyesuaian penempatan agar script dapat berjalan.
    ```javascript
    ...

    // Calculator
    var print = document.getElementById('print');
    var erase = false;

    var go = function(x) {
      if (x === 'ac') {
        /* implemetnasi clear all */
      } else if (x === 'eval') {
          print.value = Math.round(evil(print.value) * 10000) / 10000;
          erase = true;
      } else {
        print.value += x;
      }
    };

    function evil(fn) {
      return new Function('return ' + fn)();
    }
    // END

    ...
    ```
4. Implementasi fitur `AC` pada calculator.
5. _Commit_ dan _push_.

## Membuat Fitur Mengganti Tema dengan Library Select2
Langkah:
1. Import library select2 dan css select2 ke `lab_6.html`. Silakan gunakan CDN yang telah disediakan dari halaman select2.org untuk import library select2 dan css select2 pada bagian head lab_6.html
    ```html
    
    <link href="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.4/css/select2.min.css" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.4/js/select2.min.js"></script>
    
    ```
1. Buatlah sebuah elemen ```<select>``` dan apply button pada `lab_6.html`. Tambahkan elemen ```<select>``` pada halaman `lab_6.html`. Contoh:
    ```html
    
    <select class="my-select"></select>
    ...
    <button class="apply-button">apply</button>
    
    ```
    Posisikan kedua lemen tersebut dengan rapi pada halaman `lab_6.html`
1. Buka file lab_6.js tambahkan kode berikut untuk melakukan inisiasi select2
    ```javascript
    
    $(document).ready(function() {
        $('.my-select').select2();
    });
    
    ```
    Kode tersebut diperlukan untuk melakukan inisiasi select2 ke elemen ```<select>``` yang dituju. Pastikan bahwa class sesuai.
1. Lakukan inisiasi data JSON themes dan selected theme di Local Storage.
    
    `themes`
    
    ```java
    
    "[
        {"id":0,"text":"Red","bcgColor":"#F44336","fontColor":"#FAFAFA"},
        {"id":0,"text":"Pink","bcgColor":"#E91E63","fontColor":"#FAFAFA"},
        {"id":0,"text":"Purple","bcgColor":"#9C27B0","fontColor":"#FAFAFA"},
        {"id":0,"text":"Indigo","bcgColor":"#3F51B5","fontColor":"#FAFAFA"},
        {"id":0,"text":"Blue","bcgColor":"#2196F3","fontColor":"#212121"},
        {"id":0,"text":"Teal","bcgColor":"#009688","fontColor":"#212121"},
        {"id":0,"text":"Lime","bcgColor":"#CDDC39","fontColor":"#212121"},
        {"id":0,"text":"Yellow","bcgColor":"#FFEB3B","fontColor":"#212121"},
        {"id":0,"text":"Amber","bcgColor":"#FFC107","fontColor":"#212121"},
        {"id":0,"text":"Orange","bcgColor":"#FF5722","fontColor":"#212121"},
        {"id":0,"text":"Brown","bcgColor":"#795548","fontColor":"#FAFAFA"}
    ]"
    
    ```
    
    `selectedTheme`
    
    ```
    
    {"Indigo":{"bcgColor":"#3F51B5","fontColor":"#FAFAFA"}}
    
    ```
    Silakan eksplorasi cara menggunakan JSON.parse() dan JSON.stringify() pada tautan [JSON Parse](https://www.w3schools.com/js/js_json_parse.asp) dan [JSON Stringify](https://www.w3schools.com/js/js_json_stringify.asp)
1. Load JSON dari Local Storage

    Load themes dari local storage sebagai data untuk select2.
    Load selectedTheme dari local storage sebagai data untuk default theme. Nilai dari selectedTheme akan digunakan untuk default them saat page di load pertama kali.
    
    Ingat kembali cara mengambil value dari local storage seperti yang telah dicontohkan sebelumnya diatas.

1. Populate data themes untuk select2

    Populate data select2 menggunakan options ynag telah didefinisikan oleh dokumentasi select2.
    Silakan refer ke halaman [http://select2.org/data-sources/formats](https://select2.org/data-sources/formats) untuk format yang lebih jelas.
    
    ```javascript
    
    $('.my-select').select2({
        'data': JSON.parse(**ISI DENGAN DATA THEMES DARI LOCAL STORAGE**)
    })
    
    ```

    Jangan lupa untuk parse data JSON dari local storage terlebih dahulu sebelum digunakan.

1. Buat sebuah handler ketika tombol __Apply__ ditekan

    Ketika tombol apply ditekan maka theme yang dipilih harus langsung diaplikasikan ke halaman.
    Berikan handler onClick untuk elemem button Apply.
    
    ```javascript
    
    $('.apply-button-class').on('click', function(){  // sesuaikan class button
        // [TODO] ambil value dari elemen select .my-select
        
        // [TODO] cocokan ID theme yang dipilih dengan daftar theme yang ada
        
        // [TODO] ambil object theme yang dipilih
        
        // [TODO] aplikasikan perubahan ke seluruh elemen HTML yang perlu diubah warnanya
        
        // [TODO] simpan object theme tadi ke local storage selectedTheme
    })
    
    ```
    
    Jika berhasil maka warna background dan font element HTML yang dipilih akan berubah warna sesuai theme yang dipilih.
    Selain itu data selectedTheme pada local storage juga akan berubah ke theme yang telah Anda pilih.

## Unit Testing Qunit (Additional)
(Disarankan telah mengimplementasikan fitur `AC` pada calculator)
1. Tambahkan kode berikut di dalam `lab_6/layout/base.html` kalian :

    ```html
    
    <link rel="stylesheet" href="https://code.jquery.com/qunit/qunit-2.4.1.css">
    <head>
    ......
    ......
    <body>
    <div id="qunit"></div>
    ......
        <script src="{% static 'js/lab_6.js' %}"></script>
        <script src="https://code.jquery.com/qunit/qunit-2.4.1.js"></script>
    .....
    
    ```

2. _Reload_ lah halaman _web_ kalian maka kalian akan melihat di atas kalkulator akan muncul tampilan Qunit
3. Kita akan mencoba membuat _Unit Test_ untuk Kalkulator yang sudah kita buat. Buatlah sebuah file `static/js/test.js`
di dalam `lab_6` apps. Isikan kode berikut kedalam berkas tersebut
    ```javascript
        
        $( document ).ready(function() {
        var button_8 = $('button:contains("8")');
        var button_4 = $('button:contains("4")');
    
        var button_add = $('button:contains("+")');
        var button_sub = $('button:contains("-")');
        var button_mul = $('button:contains("*")');
        var button_div = $('button:contains("/")');
    
        var button_clear = $('button:contains("AC")');
        var button_res = $('button:contains("=")');
    
    
    
        QUnit.test( "Addition Test", function( assert ) {
          button_8.click();
          button_add.click();
          button_4.click();
          button_res.click();
          assert.equal( $('#print').val(), 12, "8 + 4 must be 12" );
          button_clear.click();
        });
    });
    
    ```

4. Jalankan _Page_ Lab 6 maka kalian akan melihat deskripsi bahwa _Unit Test Passed_
5. Kita akan coba tambahkan _Unit Test_ baru, namun kali ini kita akan buat _Test Case_ yang salah.
Masukkan kode berikut ke dalam `static/js/test.js`

    ```javascript
    
    .....
        QUnit.test( "Substraction Test", function( assert ) {
          button_8.click();
          button_sub.click();
          button_4.click();
          button_res.click();
          assert.equal( $('#print').val(), 12, "8 - 4 must be 4" );
          button_clear.click();
        });
    .....
    
    ```
    
6. Jalankan _Page_ Lab 6 maka kalian akan melihat deskripsi bahwa _Unit Test Fail_.
    > Sekarang kalian sudah bisa melihat perbedaan tampilan Test yang failed dengan yang passed
7. Perbaiki _Test Case_ tersebut agar _passed_
8. Sebagai pelengkap, tambahkan _Test_ berikut di dalam `static/js/test.js`
```javascript
    QUnit.test( "Multiply Test", function( assert ) {
      button_8.click();
      button_mul.click();
      button_4.click();
      button_res.click();
      assert.equal( $('#print').val(), 32, "8 * 4 must be 32" );
      button_clear.click();
    });

    QUnit.test( "Division Test", function( assert ) {
      button_8.click();
      button_div.click();
      button_4.click();
      button_res.click();
      assert.equal( $('#print').val(), 2, "8 / 4 must be 2" );
      button_clear.click();
    });
``` 
9. _Hide_ tampilan dari Qunit _report_ yang ada di dalam `lab_6/layout/base.html`
```html
.....
<div id="qunit" hidden></div>
.....
```

## Checklist

1.  Membuat Halaman Chat Box
    1. [ ] Tambahkan _lab_6.html_ pada folder templates
    2. [ ] Tambahkan _lab_6.css_ pada folder _./static/css_
    3. [ ] Tambahkan file _lab_6.js_ pada folder _lab_6/static/js_
    4. [ ] Lengkapi potongan kode pada _lab_6.js_ agar dapat berjalan

2. Mengimplementasikan Calculator
    1. [ ] Tambahkan potongan kode ke dalam file _lab_6.html_ pada folder templates
    2. [ ] Tambahkan potongan kode ke dalam file _lab_6.css_ pada folder _./static/css_
    3. [ ] Tambahkan potongan kode ke dalam file _lab_6.js_ pada folder _lab_6/static/js_
    4. [ ] Implementasi fungsi `AC`.

3.  Mengimplementasikan select2
    1. [ ] Load theme default sesuai selectedTheme
    2. [ ] Populate data themes dari local storage ke select2
    3. [ ] Local storage berisi themes dan selectedTheme
    4. [ ] Warna berubah ketika theme dipilih

4.  Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ]  Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md).
    2. [ ] Pastikan _Code Coverage_ kalian 100%.

###  Challenge Checklist
1. Latihan Qunit
    1. [ ] Implementasi dari latihan Qunit
1. Cukup kerjakan salah satu nya saja:
    1. Implementasikan tombol enter pada chat box yang sudah tersedia
        1. [ ] Buatlah sebuah _Unit Test_ menggunakan Qunit
        2. [ ] Bulah fungsi yang membuat _Unit Test_ Tersebut _passed_ 
    1. Implementasikan fungsi `sin`, `log`, dan `tan`. (HTML sudah tersedia di dalam potongan kode)
        1. [ ] Buatlah sebuah _Unit Test_ menggunakan Qunit
        2. [ ] Bulah fungsi yang membuat _Unit Test_ Tersebut _passed_
