from django.shortcuts import render

# Calculates age.
def calculate_age(birth_year):
    return 2017 - birth_year

# Enter your name here
mhs_name = 'Ichlasul Affan'
age = calculate_age(1999)

# Create your views here.
def index(request):
    response = {'name': mhs_name, 'age': age}
    return render(request, 'index.html', response)
