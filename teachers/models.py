from django.db import models
from subjects.models import Subject

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    doj = models.DateField(auto_now_add=True)
    subjects = models.ManyToManyField(Subject)
    salary = models.IntegerField()
