from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .csui_login_helper import get_access_token, verify_user

#authentication
def check_login(request, html, response):
    if 'user_login' in request.session:
        response['user_login'] = request.session["user_login"]
        return html
    else:
        response['user_login'] = ""
        return 'login.html'

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #call csui_helper
        access_token = get_access_token(username, password)
        if access_token is not None:
            ver_user = verify_user(access_token)
            kode_identitas = ver_user['identity_number']
            role = ver_user['role']

            # set session
            request.session['user_login'] = username
            request.session['access_token'] = access_token
            request.session['kode_identitas'] = kode_identitas
            request.session['role'] = role
            messages.success(request, "Login success.")
        else:
            messages.warning(request, "Wrong username or password.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def auth_logout(request):
    request.session.flush() # menghapus semua session
    messages.warning(request, "Logout successful. Your session has been removed.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))