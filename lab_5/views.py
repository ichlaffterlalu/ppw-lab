from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import Todo_Form
from .models import Todo

# Create your views here.
response = {}
def index(request):    
	response['author'] = "Ichlasul Affan" #TODO Implement yourname
	todo = Todo.objects.all()
	response['todo'] = todo
	html = 'lab_5/lab_5.html'
	response['todo_form'] = Todo_Form
	return render(request, html, response)

def add_todo(request):
	form = Todo_Form(request.POST or None)
	if(request.method == 'POST' and form.is_valid()):
		response['title'] = request.POST['title']
		response['description'] = request.POST['description']
		todo = Todo(title=response['title'],description=response['description'])
		todo.save()
		messages.add_message(request, messages.SUCCESS, "Todo has been created.", extra_tags="add")
		return HttpResponseRedirect('/lab-5/')
	else:
		for x in form.errors:
			messages.add_message(request, messages.ERROR, form.errors[x], extra_tags="add")
		return HttpResponseRedirect('/lab-5/')

def delete_todo(request):
	try:
		object = Todo.objects.get(id=request.GET.get('id',''))
		object.delete()
		messages.add_message(request, messages.SUCCESS, "Todo has been deleted.", extra_tags="delete")
	except:
		messages.add_message(request, messages.ERROR, "The todo does not exist.", extra_tags="delete")
	finally: return HttpResponseRedirect('/lab-5/#my-list')