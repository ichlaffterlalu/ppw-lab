from django.shortcuts import render
from praktikum.custom_auth import check_login

# Create your views here.
response = {}
def index(request):
    html = 'lab_8/lab_8.html'
    html = check_login(request, html, response)
    response['user_login'] = request.session.get('user_login','')
    return render(request, html, response)