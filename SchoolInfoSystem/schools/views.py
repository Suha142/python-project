from django.views import generic
from django.shortcuts import render
from django.template import loader
from .models import Admin, Places, Schools

# Create your views here.
def home(request):
    return render(request, 'schools/home.html')
def visitor(request):
    return render(request, 'schools/visitor.html')
def login(request):
    admins = Admin.objects.all()
    context = {'admins' : admins }
    return render(request, 'schools/login.html', context)
def main(request):
    y = Places.objects.all()
    z = Schools.objects.all()
    return render(request, 'schools/main.html')