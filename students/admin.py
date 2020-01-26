from django.contrib import admin
from .models import Student, PointOfContact

# Register your models here.

admin.site.register(Student)
admin.site.register(PointOfContact)