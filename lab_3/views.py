from django.shortcuts import render
# Create your views here.
diary_dict = {}
def index(request):
	return render(request, 'to_do_list.html', {'diary_dict' : diary_dict})