from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    doj = models.DateField(auto_now_add=True)
    standard = models.IntegerField()
    roll_no = models.SlugField(unique=True)
    ranking = models.IntegerField(null=True)


class PointOfContact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=12)
    relation = models.CharField(max_length=50)
    student = models.ForeignKey(Student)