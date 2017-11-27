from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Diary
from datetime import datetime
import json
from lab_login.custom_auth import check_login

# Create your views here.
diary_dict = {}
def index(request):
    diary_dict = Diary.objects.all().values()
    response = {'diary_dict' : convert_queryset_into_json(diary_dict)}

    html = 'to_do_list.html'
    html = check_login(request, 'to_do_list.html', response)
    return render(request, html, response)

def add_activity(request):
    response = {}
    dummy_response = check_login(request, False, response)
    if dummy_response: return render(request, dummy_response, response)

    # Validating content input
    if request.POST["activity"].strip() == "":
        messages.add_message(request, messages.ERROR, 'ERROR: Activity should not be empty.')
        return redirect('/lab-3/')

    try:
        date = datetime.strptime(request.POST['date'],'%Y-%m-%dT%H:%M')
        Diary.objects.create(date=date,activity=request.POST['activity'].strip())
        return redirect('/lab-3/')
    except (ValueError, OverflowError) as e:
        messages.add_message(request, messages.ERROR, 'ERROR: Date should be from 0001-01-01T00:00 to 9999-31-12T23:59.')
        return redirect('/lab-3/')

def convert_queryset_into_json(queryset):
    ret_val = []
    for data in queryset:
        ret_val.append(data)
    return ret_val