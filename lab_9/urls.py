from django.conf.urls import url
from .views import index, profile, \
    add_session_item, del_session_item, clear_session_item, \
    cookie_login, cookie_auth_login, cookie_profile, cookie_clear

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profile/$', profile, name='profile'),

    # custom auth moved to praktikum/urls.py for challenge

    #general function : solution to challenge
    url(r'^add_session_item/(?P<key>\w+)/(?P<id>\d+)/$', add_session_item, name='add_session_item'),
    url(r'^del_session_item/(?P<key>\w+)/(?P<id>\d+)/$', del_session_item, name='del_session_item'),
    url(r'^clear_session_item/(?P<key>\w+)/$', clear_session_item, name='clear_session_item'),

    # cookie
    url(r'^cookie/login/$', cookie_login, name='cookie_login'),
    url(r'^cookie/auth_login/$', cookie_auth_login, name='cookie_auth_login'),
    url(r'^cookie/profile/$', cookie_profile, name='cookie_profile'),
    url(r'^cookie/clear/$', cookie_clear, name='cookie_clear'), #sekaligus logout dari cookie
]