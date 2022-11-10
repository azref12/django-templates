
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^blog/', include('blog.urls')),
    url(r'^category/', include('category.urls')),
]
