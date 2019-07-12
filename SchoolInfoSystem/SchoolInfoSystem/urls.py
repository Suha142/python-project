from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('schools.urls')),
]
