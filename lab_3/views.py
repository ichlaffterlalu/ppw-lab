from django.shortcuts import render
from .models import Diary
from datetime import datetime
import pytz

# Create your views here.
diary_dict = {}
def index(request):
	return render(request, 'to_do_list.html', {'diary_dict' : diary_dict})

def add_activity(request):
    if request.method == 'POST':
        date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
        Diary.objects.create(date=date.replace(tzinfo=pytz.UTC),activity=request.POST['activity'])
        return redirect('/lab-3/')