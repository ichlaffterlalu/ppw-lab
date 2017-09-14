from django.shortcuts import render
from datetime import datetime, date
# Enter your name here
<<<<<<< HEAD
mhs_name = 'Ichlasul Affan'
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date(1999,3,12)
=======
mhs_name = '' # TODO Implement this
curr_year = int(datetime.now().strftime("%Y"))
birth_date = date() #TODO Implement this, format (Year, Month, Date)
>>>>>>> 6146a3717e79a7c79f6b6ffa0e210a31f03c9d8a
# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date.year)}
    return render(request, 'index_lab1.html', response)

def calculate_age(birth_year):
    return curr_year - birth_year if birth_year <= curr_year else 0
