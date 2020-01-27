from django.db import models

# Create your models here.


class ClassRoom(models.Model):
    OVAL = 'OVL'
    RECTANGLE = 'REC'
    CANOPY = 'CAN'
    ELEVATED = 'ELE'
    shape_choices = [
        (OVAL, 'Oval'),
        (RECTANGLE, 'Rectangle'),
        (CANOPY, 'Canopy'),
        (ELEVATED, 'Elevated'),
    ]
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    web_lecture_support = models.BooleanField(default=False)
    shape = models.CharField(max_length=3, choices=shape_choices)

    def __str__(self):
        return self.name
