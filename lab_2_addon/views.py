from django.shortcuts import render
from lab_1.views import mhs_name, birth_date
from praktikum.custom_auth import check_login

#My biodata
bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
{'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},\
{'subject' : 'Sex', 'value' : 'Male'}]

def index(request):
	response = {'bio_dict':bio_dict}
	html = 'description_lab2addon.html'
	html = check_login(request, html, response)
	return render(request, html, response)
