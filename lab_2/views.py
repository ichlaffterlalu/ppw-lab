from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

<<<<<<< HEAD
#Content paragraph for landing page
landing_page_content = "I am an ambitious-looked guy but I am not really that ambitious."
=======
#TODO Implement
#Create a content paragraph for your landing page:
landing_page_content = ''
>>>>>>> 6146a3717e79a7c79f6b6ffa0e210a31f03c9d8a

def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)