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
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import lab_1.urls as lab_1
import lab_2.urls as lab_2
import lab_2_addon.urls as lab_2_addon
import lab_3.urls as lab_3
import lab_4.urls as lab_4
import lab_5.urls as lab_5
import lab_6.urls as lab_6
import lab_7.urls as lab_7
import lab_8.urls as lab_8
import lab_9.urls as lab_9

# /sol
from .custom_auth import auth_login, auth_logout

urlpatterns = [
    # authentication using CSUI account
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    # admin page
    url(r'^admin/', admin.site.urls),

    # lab pages
    url(r'^lab-1/', include(lab_1,namespace='lab-1')),
    url(r'^lab-2/', include(lab_2,namespace='lab-2')),
    url(r'^lab-2-addon/', include(lab_2_addon,namespace='lab-2-addon')),
	url(r'^lab-3/', include(lab_3,namespace='lab-3')),
	url(r'^lab-4/', include(lab_4, namespace='lab-4')),
	url(r'^lab-5/', include(lab_5, namespace='lab-5')),
    url(r'^lab-6/', include(lab_6, namespace='lab-6')),
    url(r'^lab-7/', include(lab_7, namespace='lab-7')),
    url(r'^lab-8/', include(lab_8, namespace='lab-8')),
    url(r'^lab-9/', include(lab_9, namespace='lab-9')),
    url(r'^favicon.ico', RedirectView.as_view(url="/static/favicon.ico", permanent="True"), name='index'),
	url(r'^$', RedirectView.as_view(url="/lab-9/", permanent="True"), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
