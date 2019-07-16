from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = (
    path('home', views.home),
    path('login', views.login),
    path('main', views.main),
    path('visitor', views.visitor),
    path('addSchools', views.addSchools),
)