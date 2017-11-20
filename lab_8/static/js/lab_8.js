// FB initiation function
window.fbAsyncInit = () => {
  FB.init({
    appId      : '364988100591651',
    cookie     : true,
    xfbml      : true,
    version    : 'v2.11'
  });

  // implementasilah sebuah fungsi yang melakukan cek status login (getLoginStatus)
  // dan jalankanlah fungsi render dibawah, dengan parameter true jika
  // status login terkoneksi (connected)

  // Hal ini dilakukan agar ketika web dibuka, dan ternyata sudah login, maka secara
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
// Rubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
// Class-Class Bootstrap atau CSS yang anda implementasi sendiri
const render = loginFlag => {
  if (loginFlag) {
    $('#fblogin').remove();
    // Jika yang akan dirender adalah tampilan sudah login
    // Panggil Method getUserData yang anda implementasi dengan fungsi callback
    // yang menerima object user sebagai parameter.
    // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
    getUserData(user => {
      // Render tampilan profil, form input post, tombol post status, dan tombol logout
      about = "No description available.";
      if (user.about) about = user.about;
      $('#lab8').html(
        '<div class="profile" style="background:url(\'' + user.cover.source + '\')"><div class="profile-grad">' +
          '<div class="container">'+
          '<span class="pull-right">'+
          '<div class="row" id="profile-container">'+
          '<div style="float:left">'+
          '<img style="height:100px;width=100px;border-radius:50%;margin:10px 20px" class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
          '</div>'+
          '<div style="min-width:240px;float:right">'+
          '<div class="data">' +
            '<h1>' + user.name + '</h1>' +
            '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
          '</div>' +
          '</span></div>'+'</div>'+'</div>'+
        '</div></div>' +
        '<div class="container" id="feed-container">' +
        '<h2>About Me</h2><br>'+'<p>' + about + '</p>' +
        '<h2>Post ke Facebook</h2><br>'+
        '<textarea id="postInput" type="text" class="post" placeholder="Ketik Status Anda"/><br>' +
        '<span class="pull-right"><button class="postStatus" onclick="postFeed()">Post to Timeline</button></span>' +
        '<br><h2>Timeline</h2><br></div>'
      );

      // Setelah merender tampilan diatas, dapatkan data home feed dari akun yang login
      // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
      // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
      // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
      getUserFeed(feed => {
        feed.data.map(value => {
          // Render feed, kustomisasi sesuai kebutuhan.
          //jika terdapat fields message dan story pada feed
          if (value.message && value.story) {
            message = value.message.replace(/\n/g, "<br/>");
            $('#feed-container').append(
              '<div class="feed" style="position: relative;" >' +
                '<p>' + message + '</p>' +
                '<p>' + value.story + '</p>' +'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
            //jika hanya ada field message pada feed
          } else if (value.message) {
            message = value.message.replace(/\n/g, "<br/>");
            $('#feed-container').append(
              '<div class="feed" style=" position: relative;" >' +
              '<div class="row">'+
              '<div class="col-xs-1">'+
              '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
              '<div class="col-xs-10"><div class="row"><div class="row-xs-6 name">'+
              '<p>' + user.name + '</p></div>'+
              '<div class="row-xs-6 date">'+
              '<p>' + value.created_time + '</p></div></div></div> <div class="col-xs-1"></div></div>'+
              '<div class="row"><div class="col-xs-12 status-field">'+
                '<p>' + message + '</p>'+
              '</div>'+
              '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
            //jika hanya ada story pada feed
          } else if (value.story) {
            //jika story memiliki gambar dan deskripsi
            if(value.description && value.picture){
            $('#feed-container').append(
              '<div class="feed" style=" position: relative;" >' +
              '<div class="row">'+
              '<div class="col-xs-1">'+
              '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
              '<div class="col-xs-10"><div class="row"><div class="row-xs-6 name">'+
              '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">' + value.story +'</a></p></div>'+
              '<div class="row-xs-6 date">'+
              '<p>' + value.created_time + '</p></div></div></div> <div class="col-xs-1"></div></div>'+
              '<div class="row"><div class="col-xs-12 status-field">'+
                '<p>' + value.description + '</p>'+
                  '<img style="margin: 0px auto;display:block;" class="picture" src="' + value.picture + '" alt="pic" />'+
              '</div>'+
              '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
            //jika story hanya memiliki field gambar (biasanya saat update foto profil)
          }else if(value.picture){
            $('#feed-container').append(
              '<div class="feed" style=" position: relative;" >' +
              '<div class="row">'+
              '<div class="col-xs-1">'+
              '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
              '<div class="col-xs-10"><div class="row"><div class="row-xs-6 name">'+
              '<p>' + value.story + '</p></div>'+
              '<div class="row-xs-6 date">'+
              '<p>' + value.created_time + '</p></div></div></div> <div class="col-xs-1"></div></div>'+
              '<div class="row"><div class="col-xs-12 status-field">'+
                '<img style="margin: 0px auto;display:block;" class="picture" src="' + value.picture + '" alt="pic" />'+
              '</div>'+
              '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
            //jika story hanya memiliki field deskripsi (biasanya saat share suatu tautan/link)
          }else if(value.description){
            $('#feed-container').append(
              '<div class="feed" style=" position: relative;" >' +
              '<div class="row">'+
              '<div class="col-xs-1">'+
              '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
              '<div class="col-xs-10"><div class="row"><div class="row-xs-6 name">'+
              '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">' + value.story + '</a></p></div>'+
              '<div class="row-xs-6 date">'+
              '<p>' + value.created_time + '</p></div></div></div> <div class="col-xs-1"></div></div>'+
              '<div class="row"><div class="col-xs-12 status-field">'+
                '<p>' + value.description + '</p>'+
              '</div>'+
              '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
            //jika story tidak memiliki field gambar dan deskripsi (biasanya saat seseorang mengirimkan pesan pada dinding)
          }else{
            $('#feed-container').append(
              '<div class="feed" style=" position: relative;" >' +
              '<div class="row">'+
              '<div class="col-xs-1">'+
              '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
              '<div class="col-xs-10"><div class="row"><div class="row-xs-6 name">'+
              '<p>' + value.story + '</p></div>'+
              '<div class="row-xs-6 date">'+
              '<p>' + value.created_time + '</p></div></div></div> <div class="col-xs-1"></div></div>'+
              '<div class="row"><div class="col-xs-12 status-field">'+
              '</div>'+
              '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
              '</div>'
            );
          }
          }
        });
        // Logout Button
        $('#lab8').append('<button style="margin: 0px auto;display:block;background-color: blue;color: white;"" class="logout" onclick="facebookLogout()">Logout</button>');
      });
    });
  } else {
    // Tampilan ketika belum login
    $('#lab8').html('<div class="container"' +
                    '<h1 id="idle_title">Simple Facebook API Implementation</h1>' +
                    '<button id="fblogin" class="login" onclick="facebookLogin()">Login with Facebook</button>' +
                    ' Login here to use the feature.' +
                    '</div>');
  }
};

const facebookLogin = () => {
// TODO: Implement Method Ini
// Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
// ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
// pada scope yang ada.
  FB.login(function(response){
    console.log(response);
    render(response.status==='connected');
  }, {scope:'public_profile,user_posts,publish_actions,email,user_about_me,publish_pages,user_managed_groups'});
};

const facebookLogout = () => {
// TODO: Implement Method Ini
// Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
// ketika logout sukses.
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.logout();
      render(false);
    }
  });
};

const getUserData = (func) => {
// TODO: Implement Method Ini
// Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data User dari akun
// yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
// tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
// tersebut
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.api('/me?fields=id,name,cover,picture.type(large),about,email,gender', 'GET', function(response) {
        console.log(response);
        func(response);
      });
    }
  });
};

const getUserFeed = (func) => {
// TODO: Implement Method Ini
// Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
// yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
// tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
// tersebut
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.api('/me/feed?fields=story,message,full_picture,link,description,caption,name,picture,attachments,created_time', 'GET', function(response){
        console.log(response);
        func(response);
      });
    }
  });
};

const postFeed = () => {
// Todo: Implement method ini,
// Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
// Melalui API Facebook dengan message yang diterima dari parameter.
  var message = $('#postInput').val();
  FB.api('/me/feed', 'POST', {message:message});
  render(true);
};

const deletePost = (id) => {
  FB.api('/'+id, 'DELETE',function(response){
    if (response.success) {
      render(true);
    } else {
      alert("Can't remove posts that doesn't exist or already removed.");
    }
  });
};
