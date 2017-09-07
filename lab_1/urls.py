from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
	url(r'^$', index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)