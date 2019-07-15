from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Admin(models.Model):
    user_name = models.CharField(max_length=250)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.user_name

class Places(models.Model):
    user_id = models.ForeignKey(Admin,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=250)

    def __str__(self):
        return self.place_name

class Schools(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=350)
    syllabus_and_medium = models.CharField(max_length=350)
    established = models.CharField(max_length=350)
    level = models.CharField(max_length=350)
    admission_period = models.CharField(max_length=1000)
    last_year_result = models.CharField(max_length=500)

       
    def __str__(self):
        return self.name

