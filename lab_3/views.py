from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Diary
from datetime import datetime
import pytz
import json
import re
# Create your views here.
diary_dict = {}
def index(request):
    diary_dict = Diary.objects.all().values()
    return render(request, 'to_do_list.html', {'diary_dict' : convert_queryset_into_json(diary_dict)})

def add_activity(request):
    if request.method == 'POST':
        # Validating date time input using regex
        pattern = re.compile('\d\d\d\d-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]')
        if not pattern.match(request.POST['date']):
            messages.add_message(request, messages.ERROR, 'ERROR: Date should be from 0001-01-01T00:00 to 9999-31-12T23:59.')
            return redirect('/lab-3/')
        
        # Validating content input
        if request.POST["activity"] == "":
            messages.add_message(request, messages.ERROR, 'ERROR: Activity should not be empty.')
            return redirect('/lab-3/')
        
        # If input is valid
        date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
        Diary.objects.create(date=date.replace(tzinfo=pytz.UTC),activity=request.POST['activity'])
        return redirect('/lab-3/')

def convert_queryset_into_json(queryset):
    ret_val = []
    for data in queryset:
        ret_val.append(data)
    return ret_val