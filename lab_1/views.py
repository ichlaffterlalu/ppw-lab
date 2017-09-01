from django.shortcuts import render

# Enter your name here
mhs_name = 'Ichlasul Affan' # TODO Implement this

# Create your views here.
def index(request):
    response = {'name': mhs_name}
    return render(request, 'index.html', response)

# TODO Implement this to complete last checklist
def calculate_age(birth_year):
    pass
