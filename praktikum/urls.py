"""Lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import lab_1.urls as lab_1
import lab_2.urls as lab_2
from lab_1.views import index as index_lab1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lab-1/', include(lab_1,namespace='lab-1')),
    url(r'^lab-2/', include(lab_2,namespace='lab-2')),
    url(r'^$', index_lab1, name='index')
]
