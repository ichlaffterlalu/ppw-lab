# Lab 8 : Pengenalan _Pengenalan Oauth2_

CSGE602022 - Web Design & Programming (Perancangan & Pemrograman Web) @
Faculty of Computer Science Universitas Indonesia, Odd Semester 2017/2018

* * *

## Tujuan Pembelajaran

Setelah menyelesaikan tutorial ini, mahasiswa diharapkan untuk mengerti:
- Konsep OAuth2
- Penggunaan OAuth2

## Hasil Akhir Lab
- Menggunakan facebook login untuk melakukan operasi pemanggilan API Facebook.
- Menggunakan facebook login untuk menampilkan dan menyimpan data user.
- Membuat fitur untuk melakukan post ke timeline facebook melalui API Facebook.

## Pengenalan Oauth2

_OAuth 2.0 is the industry-standard protocol for authorization_

#### Apa itu Oauth2 ?
Oauth2 merupakan protokol standard industri dalam melakukan authorisasi.  Oauth2 berupa sebuah authorization framework yang bertujuan agar suatu aplikasi mendapatkan akses tertentu dari user dalam suatu platform, dimana akses tersebut dapat digunakan dalam pemanggilan API yang disediakan oleh platform tersebut. Beberapa platform yang mengimplementasikan Ouath adalah Facebook, Twitter, Google dan lain lain.  

Secara umum, Ouath2 memiliki beberapa roles, yaitu :
Resource Owner : Resource owner merupakan pengguna platform yang memberikan akses terhadap suatu aplikasi.

Resource/Authorization server :  Resource server merupakan penyedia platform, resource server berperan dalam menyediakan service Oauth2 dan API.

Client/Application : Client merupakan aplikasi, baik dalam bentuk mobile maupun web application yang ingin menggunakan API dari resource/authorization server.


#### Cara kerja Oauth2:
Secara umum, berikut merupakan tahapan implementasi oauth2 :

![abstract flow](https://assets.digitalocean.com/articles/oauth/abstract_flow.png "abstract flow")

1. Aplikasi melakukan authorization request kepada user untuk mendapatkan permission yang akan digunakan dalam mengakses service API.
2. Jika user memberikan akses kepada aplikasi, maka aplikasi akan mendapatkan authorization grant
3. Aplikasi melakukan request untuk mendapatkan access token dari authorization server dengan menggunakan authorization grant dan application identitiy
4. Jika application identity dan authorization grant sesuai, maka authorization server akan memberikan access token kepada aplikasi, dalam tahap ini authorization sudah selesai.
5. Aplikasi kemudian melakukan pemanggilan API ke resource server, dengan memberikan access token yang telah didapatkan sebelumnya
6. Jika access token sesuai, maka server akan memberikan response yang sesuai dari pemanggilan API tersebut.


#### Facebook Login
Pada tutorial lab kali ini kita akan belajar menggunakan API dari suatu social media, yaitu facebook. Facebook telah mengimplementasikan framework oauth mereka sendiri yang bernama Facebook Login, kita juga akan menggunakan javascript jdk yang telah disediakan oleh facebook agar mempermudah kita dalam authorisasi dan pemanggilan Facebook API.

Untuk menggunakan API dari facebook, pertama-tama kita harus membuat dan mendaftarkan Aplikasi kita di facebook. Berikut merupakan langkah langkah untuk mendaftarkan dan setting pada aplikasi :

1. Buka https://developers.facebook.com/
2. Daftar Sebagai Pengembang Facebook
3. Buat Aplikasi baru dengan mengklik tombol **Add a New App** dapat ditemukan di kanan atas
4. Masuk ke halaman aplikasi yang sudah dibuat dan pilih **Add Product**, kemudian tambahkan **Facebook Login**
5. Pada bagian setting silakan tambahkan platform dan pilih website, lalu sesuaikan isi dari site url. 
   Cara lain: Anda mungkin juga mendapati halaman **Quickstart**, pilih **Web** sebagai platform.
6. Applikasi telah berhasil didaftarkan.

Setelah mendaftarkan applikasi, kita akan mencoba beberapa fitur dari Facebook API dengan menggunakan oauth(Facebook Login)

*Membuat fitur login melalui facebook*

1. Membuat sebuah file `lab8.js`
Pertama-tama buatlah sebuah file `lab8.js`, lalu isi file `lab8.js` tersebut dengan potongan kode berikut

```javascript
 window.fbAsyncInit = function() {
    FB.init({
      appId      : '{your-app-id}',
      cookie     : true,
      xfbml      : true,
      version    : '{latest-api-version}'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

```

Potongan kode diatas berfungsi untuk menginisiasi dan meload terhadap javascript sdk secara asynchronuos.

_The Facebook SDK for JavaScript doesn't have any standalone files that need to be downloaded or installed, instead you simply need to include a short piece of regular JavaScript in your HTML that will asynchronously load the SDK into your pages_

_jangan lupa tambahkan `lab8.js` pada base.html anda_

2. Ganti _{your-app-id}_ dan _{latest-api-version}_ dengan **App ID** dan **Api Version** yang dapat diperoleh dari halaman **Dashboard** aplikasi di https://developers.facebook.com/ milik Anda

3. Membuat file `lab_8.html`, pada file `lab_8.html` silahkan tambahkan button login melalui Facebook

```html
<button onclick="facebookLogin()">Login with Facebook</button>
```

Kemudian tambahkan function berikut pada file `lab8.js` yang telah dibuat sebelumnya

```javascript
function facebookLogin(){
     FB.login(function(response){
       console.log(response);
     }, {scope:'public_profile'})
   }
```

Fungsi ```facebookLogin()``` tersebut akan memanggil fungsi login dari instance FB (instance dari facebook SDK) yang berfungsi untuk menguthentifikasi dan mengauthorisasi user, function FB.login() ini juga memiliki parameter scope yang berguna untuk mengatur jenis permission apa saja yang aplikasi kita inginkan, sebagai contoh di atas kita telah menambah permission ```public_profile``` agar aplikasi kita dapat mengakses id, name, first_name, last_name dll milik kita (lihat di [sini](https://developers.facebook.com/docs/facebook-login/permissions#reference-public_profile)). Kita juga dapat melihat list permission yang ada melalui tautan berikut
https://developers.facebook.com/docs/facebook-login/permissions

Fungsi di atas akan mengembalikan response sebagai berikut :

```json
{
    status: 'connected',
    authResponse: {
        accessToken: '...',
        expiresIn:'...',
        signedRequest:'...',
        userID:'...'
    }
}
```

Untuk lebih jelasnya, kita dapat melihat dokumentasi mengenai fungsi dan method yang dimiliki oleh facebook javascript sdk, melalui url berikut https://developers.facebook.com/docs/javascript/reference/v2.11

Kita juga dapat melihat list permission yang ada melalui tautan berikut
https://developers.facebook.com/docs/facebook-login/permissions

_Menampilkan informasi user_

Untuk menampilkan informasi User, kita dapat menggunakan Graph API yang dimiliki oleh Facebook, berikut merupakan contoh fungsi ```getUserData()```untuk mendapatkan informasi user

```javascript
function getUserData(){
   FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          FB.api('/me?fields=id,name', 'GET', function(response){
            console.log(response);
          });
        }
    });
}
```

Method api() pada instance FB akan melakukan request dengan method GET dan  url path ‘me?fields=id,name’ yang akan mengembalikan response sebagai berikut

```json
{
  id: "1680341582010118",
  name: "Igun Nugi"
}
```

Anda bisa menambahkan fields yang dikembalikan sesuai dengan kebutuhan, tetapi disesuaikan dengan permission yang sudah diatur saat login ke facebook (lihat kembali fungsi facebookLogin()). Detail mengenai graph API dapat dilihat pada tautan berikut https://developers.facebook.com/docs/graph-api/reference/

_Membuat Post ke timeline_

1. Mengubah fungsi facebookLogin dengan menambahkan permission yang berada pada `lab8.js` seperti pada code dibawah ini :

```javascript
function facebookLogin(){
     FB.login(function(response){
       console.log(response);
     }, {scope:'public_profile,user_posts,publish_actions'})
   }
```

Dengan menambahkan permission `user_posts` dan `publish_actions`, apa saja yang dapat dilakukan oleh aplikasi kita menggunakan Graph API?

Untuk memposting status pada timeline facebook kita dapat menggunakan Graph API yang digunakan oleh facebook, berikut merupakan contohnya

```javascript
function postFeed(){
     var message = "Hello World!";
     FB.api('/me/feed', 'POST', {message:message});
 }
```

2. Login ulang dan cobalah untuk posting sesuatu pada facebook

_Membuat Fitur logout_

Untuk membuat fitur logout kita dapat menggunakan method logout dari instance FB, berikut merupakan contoh implementasi fungsi logout

```javascript
function facebookLogout(){
     FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
          FB.logout();
        }
     });
 }

```

## Template lab8.js

Anda dapat menggunakan template lab8.js dibawah ini untuk memulai mengerjakan lab8

```javascript
  // FB initiation function
  window.fbAsyncInit = () => {
    FB.init({
      appId      : '{your app id}',
      cookie     : true,
      xfbml      : true,
      version    : '{your api version}'
    });

    // implementasilah sebuah fungsi yang melakukan cek status login (getLoginStatus)
    // dan jalankanlah fungsi render di bawah, dengan parameter true jika
    // status login terkoneksi (connected)

    // Hal ini dilakukan agar ketika web dibuka dan ternyata sudah login, maka secara
    // otomatis akan ditampilkan view sudah login
  };

  // Call init facebook. default dari facebook
  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "https://connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));

  // Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
  // merender atau membuat tampilan html untuk yang sudah login atau belum
  // Ubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
  // Class-Class Bootstrap atau CSS yang anda implementasi sendiri
  const render = loginFlag => {
    if (loginFlag) {
      // Jika yang akan dirender adalah tampilan sudah login

      // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
      // yang menerima object user sebagai parameter.
      // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
      getUserData(user => {
        // Render tampilan profil, form input post, tombol post status, dan tombol logout
        $('#lab8').html(
          '<div class="profile">' +
            '<img class="cover" src="' + user.cover.source + '" alt="cover" />' +
            '<img class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
            '<div class="data">' +
              '<h1>' + user.name + '</h1>' +
              '<h2>' + user.about + '</h2>' +
              '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
            '</div>' +
          '</div>' +
          '<input id="postInput" type="text" class="post" placeholder="Ketik Status Anda" />' +
          '<button class="postStatus" onclick="postStatus()">Post ke Facebook</button>' +
          '<button class="logout" onclick="facebookLogout()">Logout</button>'
        );

        // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
        // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
        // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
        // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
        getUserFeed(feed => {
          feed.data.map(value => {
            // Render feed, kustomisasi sesuai kebutuhan.
            if (value.message && value.story) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h1>' + value.message + '</h1>' +
                  '<h2>' + value.story + '</h2>' +
                '</div>'
              );
            } else if (value.message) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h1>' + value.message + '</h1>' +
                '</div>'
              );
            } else if (value.story) {
              $('#lab8').append(
                '<div class="feed">' +
                  '<h2>' + value.story + '</h2>' +
                '</div>'
              );
            }
          });
        });
      });
    } else {
      // Tampilan ketika belum login
      $('#lab8').html('<button class="login" onclick="facebookLogin()">Login</button>');
    }
  };

  const facebookLogin = () => {
    // TODO: Implement Method Ini
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
    // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
    // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
  };

  const facebookLogout = () => {
    // TODO: Implement Method Ini
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
    // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
  };

  // TODO: Lengkapi Method Ini
  // Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
  // lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di 
  // method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan 
  // meneruskan response yang didapat ke fungsi callback tersebut
  // Apakah yang dimaksud dengan fungsi callback?
  const getUserData = (fun) => {
    ...
    FB.api('/me?fields=....', 'GET', function (response){
      fun(response);
    });
    ...
  };

  const getUserFeed = (fun) => {
    // TODO: Implement Method Ini
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut
  };

  const postFeed = () => {
    // Todo: Implement method ini,
    // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
    // Melalui API Facebook dengan message yang diterima dari parameter.
  };

  const postStatus = () => {
    const message = $('#postInput').val();
    postFeed(message);
  };
```

Mengenai template ini, jika anda melihat syntax `() => {}`, itu adalah bentuk dari arrow function yang dikenalkan oleh JavaScript versi EcmaScript 6 atau ES6 atau ES2015. Arrow Function sebenarnya hanyalah bentuk lain dari syntax `function() {}` di JavaScript.

Syntax Arrow Function `(parameter1, parameter2) => { code }` sebenarnya hanyalah bentuk lain dari `function(parameter1, parameter 2) { code }`.

Syntax `const` merupakan bentuk lain dari `var`, akan tetapi `const` menandakan bahwa data tersebut tidak bisa diubah isinya, ada juga `let`, kebalikan dari `const` dimana data tersebut menandakan dapat diubah kedepannya. Dua bentuk ini merupakan best practice yang mulai diterapkan pada kode JavaScript versi EcmaScript 6 atau ES6 atau ES2015.

Syntax `const funcName = parameter1 => { code }` hanyalah bentuk lain dari `function funcName(parameter1) { code }`.

Untuk mengetahui lebih lanjut tentang EcmaScript 6, dapat membaca artikel http://es6-features.org

## Membuat Halaman OauthFacebook
1. Jangan lupa jalankan virtual environment kalian
2. Buatlah _apps_ baru bernama `lab_8`
3. Masukkan `lab_8` kedalam `INSTALLED_APPS`
4. Buatlah _Test_ baru kedalam `lab_8/tests.py` :
5. _Commit_ lalu _Push_ pekerjaan kalian, maka kalian akan melihat _UnitTest_ kalian akan _error_
6. Buatlah konfigurasi URL di `praktikum/urls.py` untuk `lab_8`
    ```python
        ........
        import lab_8.urls as lab_8

        urlpatterns = [
            .....
            url(r'^lab-8/', include(lab_8, namespace='lab-8')),
        ]
    ```

7. Buatlah konfigurasi URL di `lab_8/urls.py`
    ```python
    from django.conf.urls import url
    from .views import index

    urlpatterns = [
        url(r'^$', index, name='index'),
    ]
    ```

8. Mendaftarkan aplikasi ke Facebook Developer Page.
9. Implementasi fitur login seperti pada tutorial diatas dengan melengkapi `lab_8.html` dan `lab8.js`
10. Implementasi fitur post facebook pada halaman `lab_8.html` dan `lab8.js`
11. Implementasi fitur logout pada `lab_8.html` dan `lab8.js`
12. Deploy ke heroku dan jangan lupa mengganti hostname aplikasi kalian pada setting page di facebook developers admin page dengan url herokuapp kalian.
13. Jangan lupa bahagia! <3

*DISCLAIMER*
Pastikan anda menggunakan browser Google Chrome / Mozilla Firefox versi terbaru (Chrome 45++ atau Firefox 22++) karena JavaScript yang digunakan pada lab ini merupakan JavaScript modern yang tidak semua browser bisa menjalankannya.

## Checklist

### Mandatory
1. Membuat halaman untuk Login menggunakan OAuth
    1. [ ] Mendaftarkan aplikasi ke facebook developer page
    2. [ ] Melakukan OAuth Login menggunakan Facebook
    3. [ ] Menampilkan informasi dari user yang login menggunakan API Facebook.
    4. [ ] Melakukan post status facebook
    5. [ ] Menampilkan post status pada halaman lab_8.html
    6. [ ] Melakukan Logout
    7. [ ] Implementasi css yang indah dan responsive
    
2. Jawablah pertanyaan yang ada di dokumen ini dengan menuliskannya pada buku catatan atau pada source code kalian yang dapat ditunjukkan saat demo

3. Pastikan kalian memiliki _Code Coverage_ yang baik
    1. [ ] Jika kalian belum melakukan konfigurasi untuk menampilkan _Code Coverage_ di Gitlab maka lihat langkah `Show Code Coverage in Gitlab` di [README.md](https://gitlab.com/PPW-2017/ppw-lab/blob/master/README.md)
    2. [ ] Pastikan _Code Coverage_ kalian 100%


### Additional

1. Melakukan delete status pada halaman facebook
    1. [ ] Implementasi tombol delete pada daftar post status
    2. [ ] Melakukan delete post status dengan menggunakan API Facebook yang ada.
