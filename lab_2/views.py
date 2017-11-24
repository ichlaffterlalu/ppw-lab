from django.shortcuts import render
from lab_1.views import mhs_name, birth_date
from praktikum.custom_auth import check_login

#Content paragraph for landing page
landing_page_content = "I am an ambitious-looked guy but I am not really that ambitious"

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    html = 'index_lab2.html'
    html = check_login(request, html, response)
    return render(request, html, response)