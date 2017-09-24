from django.shortcuts import render
from django.contrib import messages
from lab_2.views import landing_page_content
from django.http import HttpResponseRedirect
from .forms import Message_Form
from .models import Message

# Create your views here.
response = {'author': "Ichlasul Affan"}
about_me = ['Saya sedang belajar PPW.', 'Kenapa PPW pakai Django?', 'Karena sedang belajar TDD?', 'Atau tampaknya sedang dalam proses Pythonisasi?', 'Hmm... saya bingung.', 'Tanya ke asdos atau dosennya langsung mungkin lebih baik.']
def index(request):
	response['content'] = landing_page_content
	html = 'lab_4/lab_4.html'
	response['about_me'] = about_me
	response['message_form'] = Message_Form
	return render(request, html, response)

def message_post(request):
    form = Message_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['name'] = request.POST['name'].strip() if request.POST['name'].strip() != "" else "Anonymous"
        response['email'] = request.POST['email'].strip() if request.POST['email'].strip() != "" else "Anonymous"
        response['message'] = request.POST['message'].strip()
        message = Message(name=response['name'], email=response['email'],
                          message=response['message'])
        message.save()
        html ='lab_4/form_result.html'
        return render(request, html, response)
    else:        
        for x in form.errors:
            messages.add_message(request, messages.ERROR, form.errors[x])
        return HttpResponseRedirect('/lab-4/')

def message_table(request):
	message = Message.objects.all()
	response['message'] = message
	html = 'lab_4/table.html'
	return render(request, html , response)