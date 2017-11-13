from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper
import os
import json

response = {}
csui_helper = CSUIhelper(username=os.environ.get("SSO_USERNAME", "yourusername"),
                         password=os.environ.get("SSO_PASSWORD", "yourpassword"))

def index(request):
    # Page halaman menampilkan list mahasiswa yang ada
    # TODO berikan akses token dari backend dengan menggunakaan helper yang ada

    mahasiswa_list = csui_helper.instance.get_mahasiswa_list()

    friend_list = Friend.objects.all()
    response = {"mahasiswa_list": mahasiswa_list, "friend_list": friend_list}
    html = 'lab_7/lab_7.html'
    return render(request, html, response)

def friend_list(request):
    friend_list = Friend.objects.all()
    response['friend_list'] = friend_list
    html = 'lab_7/daftar_teman.html'
    return render(request, html, response)

def friend_list_json(request):
    if request.method == 'GET':
        friend_list = list(Friend.objects.all())
        start = int(request.GET['start'])
        end = int(request.GET['end'])

        end = end if end <= len(friend_list) else len(friend_list)
        result = list()
        for i in range(start, end):
            try: result.append(model_to_dict(friend_list[i]))
            except: pass

        return HttpResponse(json.dumps(result))

@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        name = request.POST['name']
        npm = request.POST['npm']
        friend = Friend(friend_name=name, npm=npm)
        friend.save()
        data = model_to_dict(friend)
        return HttpResponse(data)

def delete_friend(request):
    if request.method == 'GET':
        try:
            friend_id = int(request.GET["friend_id"])
            obj = Friend.objects.filter(id=friend_id)
            obj.delete()
            return JsonResponse({"result":True})
        except:
            return JsonResponse({"result":False})

@csrf_exempt
def validate_npm(request):
    npm = request.POST.get('npm', None)
    data = {
        'is_taken': find_friend(npm) #lakukan pengecekan apakah Friend dgn npm tsb sudah ada
    }
    return JsonResponse(data)

def find_friend(npm):
    try:
        Friend.objects.get(npm=npm)
        return True
    except Friend.MultipleObjectsReturned:
        return True
    except Friend.DoesNotExist:
        return False

def model_to_dict(obj):
    data = serializers.serialize('json', [obj,])
    struct = json.loads(data)
    data_dict = struct[0]["fields"]
    data_dict.update({"id":obj.id})
    data = json.dumps(data_dict)
    return data