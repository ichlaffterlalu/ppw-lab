from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .csui_helper import get_access_token, verify_user

#authentication
def auth_login(request):
    print ("#==> auth_login ")

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
            messages.success(request, "Anda berhasil login")
        else:
            messages.error(request, "Username atau password salah")
    return HttpResponseRedirect(reverse('lab-9:index'))

def auth_logout(request):
    print ("#==> auth logout")
    request.session.flush() # menghapus semua session

    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('lab-9:index'))