from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
mhs_name = 'Ichlasul Affan'
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1999,3,12)
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
