from django.db import models
from django.db.models.signals import post_save
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255)
    doj = models.DateField(auto_now_add=True)
    standard = models.IntegerField()
    ranking = models.IntegerField(null=True)

    @property
    def roll_no(self):
        return self.id

    def __str__(self):
        return self.name


class PointOfContact(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=12)
    relation = models.CharField(max_length=50)
    student = models.ForeignKey(Student)


