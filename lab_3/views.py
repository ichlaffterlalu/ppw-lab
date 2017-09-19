from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Diary
from datetime import datetime
import pytz
import json
# Create your views here.
diary_dict = {}
def index(request):
    diary_dict = Diary.objects.all().values()
    return render(request, 'to_do_list.html', {'diary_dict' : convert_queryset_into_json(diary_dict)})

def add_activity(request):
        # Validating content input
        if request.POST["activity"].strip() == "":
            messages.add_message(request, messages.ERROR, 'ERROR: Activity should not be empty.')
            return redirect('/lab-3/')
        
        try:
            date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
            Diary.objects.create(date=date.replace(tzinfo=pytz.UTC),activity=request.POST['activity'])
            return redirect('/lab-3/')
        except ValueError:
            messages.add_message(request, messages.ERROR, 'ERROR: Date should be from 0001-01-01T00:00 to 9999-31-12T23:59.')
            return redirect('/lab-3/')

def convert_queryset_into_json(queryset):
    ret_val = []
    for data in queryset:
        ret_val.append(data)
    return ret_val