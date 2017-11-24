from django.shortcuts import render
from datetime import datetime, date
from praktikum.custom_auth import check_login

# Enter your name here
mhs_name = 'Ichlasul Affan'
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1999,3,12)
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    html = 'index_lab1.html'
    html = check_login(request, html, response)
    return render(request, html, response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
