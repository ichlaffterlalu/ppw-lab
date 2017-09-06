from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = ''

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)