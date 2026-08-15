from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    photo=models.ImageField(upload_to='students/photos')
    resume=models.FileField(upload_to='students/resumes')