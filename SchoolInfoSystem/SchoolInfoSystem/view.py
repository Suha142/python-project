
from django.shortcuts import render,HttpResponse

def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def main(request):
    return render(request, 'main.html')
def homepage(request):
    return HttpResponse("Hello world")