from django.shortcuts import render
from django.db.models import Prefetch
from .models import Subject
from django.db.models import Count


# Create your views here.

def teachers_gt_1(request):
    subjects = Subject.objects.annotate(num_teachers=Count('teachers')).filter(num_teachers__gt=1).prefetch_related(Prefetch('students', to_attr='student_list'))
    return render(request, 'subjects/teachers_gt_1.html', {'subjects': subjects})
