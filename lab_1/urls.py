from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
    url(r'^$', index, name='index'),
]
