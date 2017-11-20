from django.shortcuts import render

# Create your views here.
response = {}
def index(request):
    html = 'lab_8/lab_8.html'
    return render(request, html, response)