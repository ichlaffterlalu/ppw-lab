from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Friend
from .api_csui_helper.csui_helper import get_mahasiswa_list, get_detail_mhs_by_npm

from lab_login.custom_auth import check_login
import os
import json

response = {}

def index(request):
    response = {}
    dummy_response = check_login(request, False, response)
    if dummy_response: # user need to authenticate, redirect to login
        return render(request, dummy_response, response)
    else:
        # Page halaman menampilkan list mahasiswa yang ada
        # TODO berikan akses token dari backend dengan menggunakaan helper yang ada
        if request.GET.get("page") != None and request.GET.get("from") != None:
            api_response = get_mahasiswa_list(request.session['access_token'], page=request.GET.get("page",1))
            return HttpResponse(json.dumps(api_response[0]))

        else:
            api_response = get_mahasiswa_list(request.session['access_token'], page=request.GET.get("page",1))
            friend_list = list(Friend.objects.all())[-50:]
            response.update({"mahasiswa_list": api_response[0], "friend_list": friend_list,
                        "page": request.GET.get("page",1), "friend_count": Friend.objects.count(),
                        "mhs_count": api_response[1]})
            html = 'lab_7/lab_7.html'
            return render(request, html, response)

def friend_list(request):
    response['friend_list'] = Friend.objects.all()
    response['friend_count'] = Friend.objects.count()
    response['page'] = request.GET.get("page",1)
    response['per'] = request.GET.get("per",10)

    html = 'lab_7/daftar_teman.html'
    html = check_login(request, html, response)
    return render(request, html, response)

def friend_detail(request):
    dummy_response = check_login(request, False, response)
    if dummy_response: return render(request, dummy_response, response)
    elif request.method == 'GET':
        npm = request.GET.get("npm",0)
        api_response = get_detail_mhs_by_npm(request.session['access_token'], npm)
        friends = Friend.objects.filter(npm=npm)

        if len(friends) == 0: response['friend'] = False
        else: response['friend'] = friends[0]

        response['npm'] = npm
        response['alamat_mhs'] = api_response.get("alamat_mhs","-")
        response['kd_pos_mhs'] = api_response.get("kd_pos_mhs","-")
        response['kota_lahir'] = api_response.get("kota_lahir","-")
        response['tgl_lahir'] = api_response.get("tgl_lahir","-")
        try:
            response['kd_org'] = api_response["program"][0].get("kd_org","--.--.--.--")
            response['nm_org'] = api_response["program"][0].get("nm_org","-")
            response['nm_prg'] = api_response["program"][0].get("nm_prg","undefined")
            response['angkatan'] = api_response["program"][0].get("angkatan","-")
        except KeyError:
            response['kd_org'] = "-"
            response['nm_org'] = "-"
            response['nm_prg'] = "-"
            response['angkatan'] = "-"

        html = 'lab_7/detil_teman.html'
        return render(request, html, response)

def friend_list_json(request):
    if request.method == 'GET':
        friend_list = list(Friend.objects.all())
        start = int(request.GET['start'])
        end = int(request.GET['end'])

        end = end if end <= len(friend_list) else len(friend_list)
        result = list()
        for i in range(start, end):
            result.append(model_to_dict(friend_list[i]))

        http_response = HttpResponse(json.dumps(result))
        http_response = check_login(request, http_response, response)

        if type(http_response) == HttpResponse: return http_response
        else: return render(request, http_response, response)

@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        name = request.POST['name']
        npm = request.POST['npm']
        friend = Friend(friend_name=name, npm=npm)
        friend.save()
        data = model_to_dict(friend)

        http_response = HttpResponse(data)
        http_response = check_login(request, http_response, response)

        if type(http_response) == HttpResponse: return http_response
        else: return render(request, http_response, response)

def delete_friend(request):
    dummy_response = check_login(request, False, response)
    if dummy_response: # user needs to authenticate
        return render(request, dummy_response, response)
    elif request.method == 'GET':
        try:
            friend_id = int(request.GET["friend_id"])
            obj = Friend.objects.get(id=friend_id)
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

    http_response = JsonResponse(data)
    http_response = check_login(request, http_response, response)

    if type(http_response) == JsonResponse: return http_response
    else: return render(request, http_response, response)

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