from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    rollno=models.CharField(max_length=15)


class Teacher(models.Model):
    name=models.CharField(max_length=15)