from django.db import models
from django.contrib import admin
class Football(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mobile_no=models.IntegerField()
    aadhar_no=models.IntegerField()
    e_mail=models.EmailField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('name','age','mobile_no','aadhar_no','e_mail')
