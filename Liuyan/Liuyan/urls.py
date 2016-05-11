"""Liuyan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from Liuyan.views import hello
from Liuyan.views import comment
from Liuyan.views import cheer
from Liuyan.views import like
from Liuyan.views import hours_ahead
from Liuyan.views import template_test2
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', hello),
    url(r'^time/(\d{1,2})/', hours_ahead),
    url(r'^temp/', template_test2),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }), 
    url(r'^comm/', comment),
    #post
    url(r'^cheer/', cheer),
    url(r'^like/', like),
]
