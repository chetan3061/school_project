from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from classrooms.models import ClassRoom

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    chapters = models.IntegerField()
    total_duration = models.IntegerField()
    per_class_duration = models.IntegerField(
        default=30,
        validators=[MaxValueValidator(120), MinValueValidator(30)]
    )
    classroom = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING, related_name='subjects')

    def __str__(self):
        return self.name
