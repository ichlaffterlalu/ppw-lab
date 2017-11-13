from django.conf.urls import url
from .views import index, add_friend, validate_npm, friend_list, delete_friend, friend_list_json

urlpatterns = [
        url(r'^$', index, name='index'),
        url(r'^add-friend/$', add_friend, name='add-friend'),
        url(r'^validate-npm/$', validate_npm, name='validate-npm'),
        url(r'^friend-list/$', friend_list, name='friend-list'),
        url(r'^delete-friend/$', delete_friend, name='delete-friend'),
        url(r'^get-friend-list/$', friend_list_json, name='get-friend-list')
]