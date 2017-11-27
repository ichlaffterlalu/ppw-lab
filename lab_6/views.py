from django.shortcuts import render
from lab_login.custom_auth import check_login

# Create your views here.
response = {}
def index(request):
	response['author'] = "Ichlasul Affan" #TODO Implement yourname
	html = 'lab_6/lab_6.html'
	html = check_login(request, html, response)
	return render(request, html, response)