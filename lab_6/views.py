from django.shortcuts import render

# Create your views here.
response = {}
def index(request):
	response['author'] = "Ichlasul Affan" #TODO Implement yourname
	html = 'lab_6/lab_6.html'
	return render(request, html, response)