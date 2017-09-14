<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> 6146a3717e79a7c79f6b6ffa0e210a31f03c9d8a
from django.conf.urls import url
from .views import index
#url for app
urlpatterns = [
<<<<<<< HEAD
	url(r'^$', index, name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^$', index, name='index'),
]
>>>>>>> 6146a3717e79a7c79f6b6ffa0e210a31f03c9d8a
