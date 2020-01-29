from django.db import models
from subjects.models import Subject

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    doj = models.DateField()
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    salary = models.IntegerField()
    takes_web_lecture = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    @property
    def teacher_subjects(self):
        if hasattr(self, '_prefetched_objects_cache'):
            return self._prefetched_objects_cache['subjects']

