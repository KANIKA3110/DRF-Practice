from django.db import models

# Create your models here.
#name price discount duration authorname

class Course(models.Model):
    name= models.CharField(max_length=30)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    duration=models.CharField(max_length=10)
    author_name=models.CharField(max_length=30)