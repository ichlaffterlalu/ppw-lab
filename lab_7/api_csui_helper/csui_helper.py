from praktikum.csui_login_helper import get_client_id
import requests

API_MAHASISWA_LIST_URL = "https://api.cs.ui.ac.id/siakngcs/mahasiswa-list/"
API_MAHASISWA_DETIL_URL = "https://api.cs.ui.ac.id/siakngcs/mahasiswa/"

def get_mahasiswa_list(access_token, page=1):
    response = requests.get(API_MAHASISWA_LIST_URL,
                            params={"access_token": access_token, "client_id": get_client_id(), "page":page})
    json_response = response.json()
    mahasiswa_list = json_response["results"]
    count = json_response["count"]
    return (mahasiswa_list, count)

def get_detail_mhs_by_npm(access_token, npm=0):
    response = requests.get(API_MAHASISWA_DETIL_URL+str(npm)+"/",
                            params={"access_token": access_token, "client_id": get_client_id()})
    json_response = response.json()
    return json_response