import requests

DRONE_API       = 'https://www.enterkomputer.com/api/product/drone.json'
SOUNDCARD_API   = 'https://www.enterkomputer.com/api/product/soundcard.json'
OPTICAL_API     = 'https://www.enterkomputer.com/api/product/optical.json'

def get_drones():
    drones = requests.get(DRONE_API)
    return drones

# lengkapi pemanggilan utk SOUNDCARD_API dan OPTICAL_API untuk mengerjakan CHALLENGE
def get_soundcards():
    soundcard = requests.get(SOUNDCARD_API)
    return soundcard
def get_opticals():
    optical = requests.get(OPTICAL_API)
    return optical