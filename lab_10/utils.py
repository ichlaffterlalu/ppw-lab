from .models import Pengguna, MovieKu
from .omdb_api import get_detail_movie

def check_movie_in_database(request, kode_movie):
    is_exist = False
    kode_identitas = request.session.get('kode_identitas')
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    count_movie = MovieKu.objects.filter(pengguna=pengguna, kode_movie=kode_movie).count()
    if count_movie > 0 :
        is_exist = True

    return is_exist

def check_movie_in_session(request, kode_movie):
    is_exist = False
    ssn_key = request.session.keys()
    if 'movies' in ssn_key:
        movies = request.session['movies']
        if kode_movie in movies:
            is_exist = True

    return is_exist

def add_item_to_database(request, id):
    kode_identitas = request.session.get('kode_identitas')
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    movieku = MovieKu()
    movieku.kode_movie = id
    movieku.pengguna = pengguna
    movieku.save()

def add_item_to_session(request, id):
    ssn_key = request.session.keys()
    if not 'movies' in ssn_key:
        request.session['movies'] = [id]
    else:
        movies = request.session['movies']
        # check apakah di session sudah ada key yang sama
        if id not in movies:
            movies.append(id)
            request.session['movies'] = movies

def create_new_user(request):
    nama = request.session.get('user_login')
    kode_identitas = request.session.get('kode_identitas')

    pengguna = Pengguna()
    pengguna.kode_identitas = kode_identitas
    pengguna.nama = nama
    pengguna.save()

    return pengguna

def get_parameter_request(request):
    if request.GET.get("judul"):
        judul = request.GET.get("judul")
    else:
        judul = "-"

    if request.GET.get("tahun"):
        tahun = request.GET.get("tahun")
    else:
        tahun = "-"

    return judul, tahun

# after login, save movies from session
def save_movies_to_database(pengguna, list_movie_id):
    #looping get id, cek apakah exist berdasarkan user, jika tidak ada, maka tambah

    for movie_id in list_movie_id:
        if not (MovieKu.objects.filter(pengguna = pengguna, kode_movie = movie_id).count()) > 0:
            new_movie = MovieKu()
            new_movie.pengguna = pengguna
            new_movie.kode_movie = movie_id
            new_movie.save()

#return movies user from db
def get_my_movies_from_database(request):
    resp = []
    kode_identitas = request.session.get('kode_identitas')
    pengguna = Pengguna.objects.get(kode_identitas=kode_identitas)
    items = MovieKu.objects.filter(pengguna=pengguna)
    for item in items:
        resp.append(item.kode_movie)
    return resp

#get my movies from session
def get_my_movies_from_session(request):
    resp = []
    ssn_key = request.session.keys()
    if 'movies' in ssn_key:
        resp = request.session['movies']
    return resp

#get detail list movie from api
def get_list_movie_from_api(my_list):
    list_movie = []
    for movie in my_list:
        list_movie.append(get_detail_movie(movie))

    return list_movie