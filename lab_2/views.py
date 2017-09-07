from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#Content paragraph for landing page
landing_page_content = "Hello, my name is Ichlasul Affan! I'm an ambitious-looked guy but I'm not really that ambitious."

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)