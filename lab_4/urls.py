from django.conf.urls import url
from .views import index, message_post


urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_message', message_post, name='add_message')
]