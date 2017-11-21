// FB initiation function
window.fbAsyncInit = () => {
  FB.init({
    appId      : '364988100591651',
    cookie     : true,
    xfbml      : true,
    version    : 'v2.11'
  });
};

var previous = "";
var next = "";
var user = {};


// Call init facebook. default dari facebook
(function(d, s, id){
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {return;}
  js = d.createElement(s); js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Functuon to print user data to the webpage
const renderData = user => {
  // Render tampilan profil, form input post, tombol post status, dan tombol logout
  $('#lab8').html("");
  about = "No description available.";
  if (user.about) about = user.about;
  $('#lab8').html(
    '<div class="profile" style="background:url(\'' + user.cover.source + '\')"><div class="profile-grad">' +
      '<div class="container">'+
      '<span class="float-right">'+
      '<div class="row" id="profile-container">'+
      '<div style="float:left">'+
      '<img style="height:100px;width=100px;border-radius:50%;margin:10px" class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
      '</div>'+
      '<div class="data" style="min-width:240px;height:100px;margin:10px;float:right">'+
        '<h2 style="line-height:48px">' + user.name + '</h2>' +
        '<h5 style="line-height:28px">' + user.email + ' - ' + user.gender + '</h5>' +
      '</div></span>'+'</div>'+'</div>'+
    '</div></div>' +
    '<div class="container" id="about-container">' +
    '<h2 id="about-me">About Me</h2>'+'<p>' + about + '</p><br>' +
    '<h2 id="post-field">Post ke Facebook</h2>'+
    '<textarea id="postInput" type="text" class="post" placeholder="Ketik Status Anda"/><br>' +
    '<span class="float-right"><button class="postStatus" onclick="postFeed()">Post to Timeline</button></span>' +
    '<br/><br/><br/><h2 id="timeline" style="float:left">Timeline</h2>'+
    '<div class="pagination" style="float:right">'+
    '<a id="to-prev" onclick="renderPrevious()">&laquo;</a><a id="to-next" onclick="renderNext()">&raquo;</a>'+
    '</div></div><br/><br/><div class="container" id="feed-container">'
  );

  // Get user feed and render it
  getUserFeed(renderFeed);

  // Logout button
  $('#lab8').append('<button id="fblogout" onclick="facebookLogout()">Logout</button>');
};

// Function to print feed to the webpage
const renderFeed = feed => {
  previous = feed.paging.previous;
  next = feed.paging.next;

  $('#feed-container').html("");
  feed.data.map(value => {
    // Render feed, kustomisasi sesuai kebutuhan.
    //jika terdapat fields message dan story pada feed
    if (value.message && value.story) {
      message = value.message.replace(/\n/g, "<br/>");
      $('#feed-container').append(
        '<div class="feed" style="position: relative;">' +
          '<p>' + message + '</p>' +
          '<p>' + value.story + '</p>' +'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
        '</div>'
      );
      //jika hanya ada field message pada feed
    } else if (value.message) {
      message = value.message.replace(/\n/g, "<br/>");
      $('#feed-container').append(
        '<div class="feed" style=" position: relative;">' +
        '<div class="row">'+
        '<div class="col-1">'+
        '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
        '<div class="col-10"><div class="row"><div class="row-6 feed-header">'+
        '<p>' + user.name + '<br/>' + value.created_time + '</p></div></div></div> <div class="col-1"></div></div>'+
        '<div class="row"><div class="col-12 status-field">'+
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
        '<div class="feed" style=" position: relative;">' +
        '<div class="row">'+
        '<div class="col-1">'+
        '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
        '<div class="col-10"><div class="row"><div class="row-6 feed-detail">'+
        '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">' + value.story +
        '</a><br/>'+ value.created_time + '</p></div></div></div> <div class="col-1"></div></div>'+
        '<div class="row"><div class="col-xs-4 col-md-2 status-field"><img class="picture" src="' + value.picture + '" alt="pic" /></div>' +
        '<div class="col-xs-7 col-md-9 status-field">'+
          '<p>' + value.description + '</p>'+
          '</div></div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
        '</div>'
      );
      //jika story hanya memiliki field gambar (biasanya saat update foto profil)
      }else if(value.picture){
        $('#feed-container').append(
          '<div class="feed" style=" position: relative;">' +
          '<div class="row">'+
          '<div class="col-1">'+
          '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
          '<div class="col-10"><div class="row"><div class="row-6 feed-header">'+ '<p>' + value.story + '<br/>'+
          value.created_time + '</p></div></div></div> <div class="col-1"></div></div>'+
          '<div class="row"><div class="col-12 status-field">'+
            '<img style="margin: 0px auto;display:block;" class="picture" src="' + value.picture + '" alt="pic" />'+
          '</div>'+
          '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
          '</div>'
        );
        //jika story hanya memiliki field deskripsi (biasanya saat share suatu tautan/link)
        }else if(value.description){
          $('#feed-container').append(
            '<div class="feed" style=" position: relative;">' +
            '<div class="row">'+
            '<div class="col-1">'+
            '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
            '<div class="col-10"><div class="row"><div class="row-6 feed-detail">'+
            '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">' + value.story + '</a><br/>'+
            value.created_time + '</p></div></div></div> <div class="col-1"></div></div>'+
            '<div class="row"><div class="col-12 status-field">'+
              '<p>' + value.description + '</p>'+
            '</div>'+
            '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
            '</div>'
          );
          //jika story tidak memiliki field gambar dan deskripsi (biasanya saat seseorang mengirimkan pesan pada dinding)
        }else{
          $('#feed-container').append(
            '<div class="feed" style=" position: relative;">' +
            '<div class="row">'+
            '<div class="col-1">'+
            '<img style="height:50px;width=50px;" class="picture" src="' + user.picture.data.url + '" alt="profpic" /></div>'+
            '<div class="col-10"><div class="row"><div class="row-6 feed-detail">'+ value.story + '<br/>'+
            value.created_time + '</p></div></div></div> <div class="col-1"></div></div>'+
            '<div class="row"><div class="col-12 status-field">'+
            '</div>'+
            '</div>'+'<span onclick="deletePost(\'' + value.id + '\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
            '</div>'
          )
        }
      }
    }
  )
};

// Retrieves loginFlag to determine what should be rendered to web
const render = loginFlag => {
  if (loginFlag) {
    getUserData(renderData);
  } else {
    // Tampilan ketika belum login
    user = {};
    $('#lab8').html('<div class="container">' +
                    '<h1 id="idle_title">Simple Facebook API Implementation</h1>' +
                    '<button id="fblogin" class="login" onclick="facebookLogin()">Login with Facebook</button>' +
                    ' Login here to use the feature.' +
                    '</div>');
  }
};

const facebookLogin = () => {
  FB.login(function(response){
    console.log(response);
    render(response.status==='connected');
  }, {scope:'public_profile,user_posts,publish_actions,email,user_about_me,publish_pages,user_managed_groups'});
};

const facebookLogout = () => {
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.logout();
      render(false);
    }
  });
};

const getUserData = (func) => {
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.api('/me?fields=id,name,cover,picture.type(large),about,email,gender', 'GET', function(response) {
        console.log(response);
        user = response;
        func(response);
      });
    }
  });
};

const getUserFeed = (func) => {
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      FB.api('/me/feed?fields=story,message,full_picture,link,description,caption,name,picture,attachments,created_time', 'GET', function(response){
        console.log(response);
        func(response);
      });
    }
  });
};

const renderPrevious = () => {
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      console.log(response);
      FB.api(previous, 'GET', function(response){
        renderFeed(response);
      });
    }
  });
}

const renderNext = () => {
  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      console.log(response);
      FB.api(next, 'GET', function(response){
        renderFeed(response);
      });
    }
  });
}

const postFeed = () => {
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
