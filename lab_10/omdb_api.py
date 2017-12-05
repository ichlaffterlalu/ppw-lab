import requests
API_KEY = "8df7c7e5" #TODO Implement, fill your OMDB API Key Here

def search_movie(judul, tahun):
    get_tahun = ""
    if not tahun == "-":
        get_tahun = "&y="+tahun
    url = "http://www.omdbapi.com/?s=" + judul + get_tahun + "&apikey=" + API_KEY
    req = requests.get(url)
    resp = req.json()

    data_exist = False
    stResponse = resp['Response']
    if stResponse == "True":
        count_results = resp['totalResults']

        #cukup ambil 30 data saja
        cp = (int(count_results) // 10)
        if cp > 3: pages = 3
        elif cp > 0 and cp <= 3: pages = cp
        else: pages = 1
        data_exist = True

    past_url = url
    all_data = []
    if data_exist:
        for page in range(pages):
            page += 1
            get_page = "&page="+str(page)
            new_url = past_url + get_page;
            new_req = requests.get(new_url).json()
            get_datas = new_req['Search']
            for data in get_datas:
                all_data.append(data)

    return all_data

def get_detail_movie(id):
    url = "http://www.omdbapi.com/?i="+id+"&apikey="+API_KEY
    req = requests.get(url)
    rj = req.json() # dict
    my_list = create_json_from_dict(rj)

    return my_list

def create_json_from_dict(your_dict):
    your_data = {}
    for key in your_dict:
        cvalue = (your_dict.get(key))
        nk = str(key).lower()
        if type(cvalue) == list:
            nv = cvalue
        else:
            nv = cvalue.encode('ascii','ignore')
        your_data[nk] = nv
    return your_data