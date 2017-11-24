// FB initiation function
window.fbAsyncInit = () => {
  FB.init({
    appId: '364988100591651',
    cookie: true,
    xfbml: true,
    version: 'v2.11'
  });

  FB.getLoginStatus(function (response) {
    render(response.status === 'connected');
  });
};

var previous = "";
var next = "";
var user = {};

// Call init facebook. default dari facebook
(function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) {
    return;
  }
  js = d.createElement(s);
  js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Function to print user data to the webpage
const renderData = user => {
  $('#lab8').html(""); // Remove #lab8 html content

  // Check if the user has "about" description
  about = "No description available.";
  if (user.about) about = user.about;

  // Render the page heads (cover, about me, textbox) to #lab8
  $('#lab8').html(
    '<div class="profile" style="background:url(\''+user.cover.source+'\')"><div class="profile-grad">'+
    '<div class="container"><span class="float-right">'+
    '<div class="row" id="profile-container"><div style="float:left">'+
    '<img style="height:100px;width=100px;border-radius:50%;margin:10px" class="picture" src="'+
    user.picture.data.url+'" alt="profpic" /></div>'+
    '<div class="data" style="min-width:240px;height:100px;margin:10px;float:right">'+
    '<h2 style="line-height:48px">'+user.name+'</h2>'+
    '<h5 style="line-height:28px">'+user.email+' - '+user.gender+'</h5>'+
    '</div></span></div></div></div></div>'+
    '<div class="container" id="about-container">'+
    '<h2 id="about-me">About Me</h2><br/>'+'<p>'+about+'</p><br/>'+
    '<h2 id="post-field">Post ke Facebook</h2>'+
    '<textarea id="postInput" type="text" class="post" placeholder="Ketik Status Anda"/><br>'+
    '<span class="float-right"><button class="postStatus" onclick="postFeed()">Post to Timeline</button></span>'+
    '<br/><br/><br/><h2 id="timeline" style="float:left">Timeline</h2>'+
    '<div class="pagination" style="float:right">'+
    '<a id="to-prev" onclick="renderPrevious()">&laquo;</a><a id="to-next" onclick="renderNext()">&raquo;</a>'+
    '</div></div><br/><br/><div class="container" id="feed-container">'
  );

  // Get user feed and render it
  getUserFeed(renderFeed);

  // Logout button
  $('#lab8').append('<button id="fblogout" onclick="facebookLogout()">Logout FB</button>');
};

// Function to print feed to the webpage
const renderFeed = feed => {
  // Save the previous page and next page address to global var
  previous = feed.paging.previous;
  next = feed.paging.next;

  $('#feed-container').html(""); // Empty #feed-container
  // For every feed item, render (append) to #feed-container
  feed.data.map(value => {
    // Formatting the created_time
    created_time = value.created_time.replace("T",", ").replace("+0000","");

    if (value.message && value.story) { // If feed item has message and story
      message = value.message.replace(/\n/g, "<br/>");
      $('#feed-container').append(
        '<div class="feed" style="position:relative;">'+
        '<p>'+message+'</p>'+
        '<p>'+value.story+'</p>'+'<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
        '</div>'
      );
    } else if (value.message) { // If feed item has message only
      message = value.message.replace(/\n/g, "<br/>");
      $('#feed-container').append(
        '<div class="feed" style="position:relative;">'+
        '<div class="row"><div class="col-4 col-md-2 col-lg-1">'+
        '<img style="height:50px;width=50px;" class="picture" src="'+user.picture.data.url+'" alt="profpic" /></div>'+
        '<div class="col-7 col-md-9 col-lg-10"><div class="row"><div class="row-6 feed-header">'+
        '<p>'+user.name+'<br/>'+created_time+'</p></div></div></div> <div class="col-4 col-md-2 col-lg-1"></div></div>'+
        '<div class="row"><div class="col-12 status-field"><p>'+message+'</p></div></div>'+
        '<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove">'+
        '</span></div>'
      );
    } else if (value.story) { // If feed item has story only
      if (value.description && value.picture) { // If feed item has description and picture
        $('#feed-container').append(
          '<div class="feed" style="position:relative;">'+
          '<div class="row"><div class="col-4 col-md-2 col-lg-1">'+
          '<img style="height:50px;width=50px;" class="picture" src="'+user.picture.data.url+'" alt="profpic" /></div>'+
          '<div class="col-7 col-md-9 col-lg-10"><div class="row"><div class="row-6 feed-detail">'+
          '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">'+value.story+
          '</a><br/>'+created_time+'</p></div></div></div> <div class="col-4 col-md-2 col-lg-1"></div></div>'+'<div class="row">'+
          '<div class="col-5 col-xs-3 col-md-2 status-field"><img class="picture" src="'+value.picture+'" alt="pic" />'+
          '</div><div class="col-6 col-xs-8 col-md-9 status-field"><p>'+value.description+'</p></div></div>'+
          '<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
          '</div>'
        );
      } else if (value.picture) { // If feed item has picture only
        $('#feed-container').append(
          '<div class="feed" style="position:relative;">'+
          '<div class="row"><div class="col-4 col-md-2 col-lg-1">'+
          '<img style="height:50px;width=50px;" class="picture" src="'+user.picture.data.url+'" alt="profpic" /></div>'+
          '<div class="col-7 col-md-9 col-lg-10"><div class="row"><div class="row-6 feed-header">'+'<p>'+value.story+'<br/>'+
          created_time+'</p></div></div></div> <div class="col-4 col-md-2 col-lg-1"></div></div>'+
          '<div class="row"><div class="col-12 status-field">'+
          '<img style="margin:0px auto;display:block;" class="picture" src="'+value.picture+'" alt="pic" />'+
          '</div>'+
          '</div>'+'<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
          '</div>'
        );
      } else if (value.description) { // If feed item has description only
        $('#feed-container').append(
          '<div class="feed" style="position:relative;">'+
          '<div class="row"><div class="col-4 col-md-2 col-lg-1">'+
          '<img style="height:50px;width=50px;" class="picture" src="'+user.picture.data.url+'" alt="profpic" /></div>'+
          '<div class="col-7 col-md-9 col-lg-10"><div class="row"><div class="row-6 feed-detail">'+
          '<p><a href="'+value.link+'" class="post-link" id="link-'+value.id+'">'+value.story+'</a><br/>'+
          created_time+'</p></div></div></div> <div class="col-4 col-md-2 col-lg-1"></div></div>'+
          '<div class="row"><div class="col-12 status-field">'+
          '<p>'+value.description+'</p></div></div>'+
          '<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
          '</div>'
        );
      } else { // If feed item has no attributes (usually when somebody else sent a message)
        $('#feed-container').append(
          '<div class="feed" style="position:relative;">'+
          '<div class="row"><div class="col-4 col-md-2 col-lg-1">'+
          '<img style="height:50px;width=50px;" class="picture" src="'+user.picture.data.url+'" alt="profpic" /></div>'+
          '<div class="col-7 col-md-9 col-lg-10"><div class="row"><div class="row-6 feed-detail">'+value.story+'<br/>'+
          created_time+'</p></div></div></div> <div class="col-4 col-md-2 col-lg-1"></div></div>'+
          '<div class="row"><div class="col-12 status-field"></div></div>'+
          '<span onclick="deletePost(\''+value.id+'\')" data-id="'+value.id+'" class="glyphicon glyphicon-remove"></span>'+
          '</div>'
        )
      }
    }
  })
};

// Function to render main login page, when not logged in
const renderNotLoggedIn = () => {
  user = {};
  $('#lab8').html('<div class="container">'+
    '<h1 id="idle_title">Simple Facebook API Implementation</h1>'+
    '<button id="fblogin" class="login" onclick="facebookLogin()"><img src="/static/img/glyphicons/facebook.png" style="margin:5px">'+
    'Login with Facebook</button> Login here to use the feature.</div>');
    $("#nav-log-fb").html('<img src="/static/img/glyphicons/facebook.png"> Login');
    $("#nav-log-fb").attr("onclick", "facebookLogin()");
};

// Retrieves loginFlag to determine what should be rendered to web
const render = loginFlag => {
  if (loginFlag) {
    getUserData(renderData); // Get user data, and render it

    // Change log button in navbar to "Logout"
    $("#nav-log-fb").html('<img src="/static/img/glyphicons/facebook.png"> Logout FB');
    $("#nav-log-fb").attr("onclick", "facebookLogout()");
  } else {
    renderNotLoggedIn(); // Renders main login page
  }
};

const facebookLogin = () => {
  FB.login(function (response) { // Login to facebook
    render(response.status === 'connected'); // Render depends on the success status of login
  }, {
    scope: 'public_profile,user_posts,publish_actions,email,user_about_me,publish_pages,user_managed_groups'
  });
};

const facebookLogout = () => {
  FB.getLoginStatus(function (response) {
    if (response.status === 'connected') {
      FB.logout(); // Logout from Facebook
      render(false); // Renders main login page
    }
  });
};

// Function to get currently logged in user's data
const getUserData = (func) => {
  FB.getLoginStatus(function (response) { // Get login status
    if (response.status === 'connected') { // If user has logged in
      FB.api('/me?fields=id,name,cover,picture.type(large),about,email,gender', 'GET', function (response) {
        user = response; // Save the response to global variable, for easy access when rendering feed
        func(response); // Callback function
      });
    }
  });
};

// Function to get currently logged in user's feed (wall/timeline)
const getUserFeed = (func) => {
  FB.getLoginStatus(function (response) { // Get login status
    if (response.status === 'connected') { // If user has logged in
      FB.api("/me/feed?fields=story,message,full_picture,link,description,caption,name,picture,attachments,created_time", 'GET', function (response) {
        func(response); // Callback function
      });
    }
  });
};

// Function to get currently logged in user's feed (wall/timeline), on previous page
const renderPrevious = () => {
  FB.getLoginStatus(function (response) { // Get login status
    if (response.status === 'connected') { // If user has logged in
      FB.api(previous, 'GET', function (response) { // Get previous page
        renderFeed(response); // Render the page
      });
    }
  });
}

// Function to get currently logged in user's feed (wall/timeline), on next page
const renderNext = () => {
  FB.getLoginStatus(function (response) { // Get login status
    if (response.status === 'connected') { // If user has logged in
      FB.api(next, 'GET', function (response) { // Get previous page
        renderFeed(response); // Render the page
      });
    }
  });
}

// Function to post a new feed in timeline/wall
const postFeed = () => {
  var message = $('#postInput').val(); // Get message from user input
  FB.api('/me/feed', 'POST', { // Post to feed
    message: message
  });
  getUserData(renderData); // Render whole page
};

// Function to delete a feed item in timeline/wall
const deletePost = (id) => {
  FB.api('/'+id, 'DELETE', function (response) {
    if (response.success) { // If response success, render whole page
      getUserFeed(renderFeed);
    } else { // Else, show error alert
      alert("Can't remove posts that doesn't exist, or not made using this app.");
    }
  });
};