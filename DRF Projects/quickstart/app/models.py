from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email= models.EmailField()
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=10, null=True, blank=True)
    
class User(models.Model):
    username=models.CharField(max_length=30)
    email= models.EmailField()
    password=models.CharField(max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)