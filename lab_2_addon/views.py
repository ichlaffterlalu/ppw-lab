from django.shortcuts import render
from lab_1.views import mhs_name, birth_date

#My biodata
bio_dict = [{'subject' : 'Name', 'value' : mhs_name},\
{'subject' : 'Birth Date', 'value' : birth_date.strftime('%d %B %Y')},\
{'subject' : 'Sex', 'value' : 'Male'}]

def index(request):
	response = {}
	return render(request, 'description_lab2addon.html', response)
