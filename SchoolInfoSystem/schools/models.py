from django.db import models

# Create your models here.
class Admin(models.Model):
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=500)

class Places(models.Model):
    user_id = models.ForeignKey(Admin,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=250)

class Schools(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=350)
    syllabus_and_medium = models.CharField(max_length=350)
    established = models.CharField(max_length=350)
    level = models.CharField(max_length=350)
    admission_period = models.CharField(max_length=1000)
    last_year_result = models.CharField(max_length=500)

