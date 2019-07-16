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
    s1 = Schools.objects.filter(location__contains='armg')
    s2 = Schools.objects.filter(location__contains='hammadpur')
    s3 = Schools.objects.filter(location__contains='anmondi')
    s4 = Schools.objects.filter(location__contains='ulshan')
    s5 = Schools.objects.filter(location__contains='nani')
    s6 = Schools.objects.filter(location__contains='tijheel')
    s7 = Schools.objects.filter(location__contains='ari')
    s8 = Schools.objects.filter(location__contains='irpur')
    s9 = Schools.objects.filter(location__contains='ttara')
    s10 = Schools.objects.filter(location__contains='bo')
    a = Admin.objects.all()
    context = {'all_schools': s,
               'in_farmgate': s1,
               'in_mdpur': s2,
               'in_dhanmondi': s3,
               'in_gulshan': s4,
               'in_bonani': s5,
               'in_motjhl': s6,
               'in_wari': s7,
               'in_mirpur': s8,
               'in_uttara': s9,
               'in_bashaboo': s10,
               'user': a}
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