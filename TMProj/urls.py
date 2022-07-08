from django.contrib import admin
from django.urls import re_path as url
from TMTsys import views as TMTsys_views
from TMTsys import urls as TMTsys_urls
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include(TMTsys_urls)),
    
    ]
