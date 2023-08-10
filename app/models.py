from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    School_name=models.CharField(max_length=100)
    Princeple_name=models.CharField(max_length=100)
    Location=models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.School_name
    
    def get_absolute_url(self):
        return reverse('SchoolDetails',kwargs={'pk':self.pk})


class Student(models.Model):
    Student_name=models.CharField(max_length=100)
    Age=models.IntegerField()
    School_name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='panda')


    def __str__(self) -> str:
        return self.Student_name
