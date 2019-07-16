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
    return render(request, 'schools/login.html')
def main(request):
    s = Schools.objects.all()
    context = {'all_schools': s}
    return render(request, 'schools/main.html' , context)
def addSchools(request):
    if "add" in request.method == 'post':
        x1 = request.post['name']
        x2 = request.post['location']
        x3 = request.post['syllabus_and_medium']
        x4 = request.post['established']
        x5 = request.post['level']
        x6 = request.post['admission_period']
        x7 = request.post['last_year_result']

        obj = Schools(name = x1, location = x2, syllabus_and_medium = x3, established = x4, level = x5, admission_period = x6, last_year_result = x7)
        obj.save()
        return render(request, 'schools/main.html')
    else:
        return render(request, 'schools/addSchools.html')