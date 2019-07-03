

from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', view.home),
    path('login', view.login),
    path('main', view.main),
    path('homepage', view.homepage)
]
