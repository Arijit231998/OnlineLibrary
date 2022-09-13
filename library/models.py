from distutils.command.upload import upload
from typing_extensions import Self
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models. PositiveIntegerField()
    category=models.CharField(max_length=100)

def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'   

class Student (models.Model):
        user= models.OneToOneField(User,on_delete=models.CASCADE)
        classroom= models.CharField(max_length=40)
        branch=models.CharField(max_length=40)
        roll_no= models.CharField(max_length=8,blank=True)
        phone=models.CharField(max_length=11,blank=True)
        image= models.ImageField(upload_to="", blank=True)
       
def __str__(self):
    return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'

def expirey():
    return str(self.user)+"[+str(self.branch)+']"

class IssuedBook(models.Model):
    student_id= models.CharField(max_length=100,blank=True)
    isbn=models.CharField(max_length=13)
    issued_date=models.DateField(auto_now=True)
    expire_date=models.DateField(default=expire)


