from django.conf.urls import url
from .views import index, add_todo

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^add_todo', add_todo, name='add_todo'),
]
