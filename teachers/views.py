from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Teacher
from students.models import Student
from subjects.models import Subject
from django.db.models import Prefetch


# Create your views here.


class TeacherList(TemplateView):
    template_name = 'teachers/teachers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher_list = list(self.class_room_data())
        context['teacher_list'] = teacher_list
        return context

    def class_room_data(self):
        queryset = Subject.objects.only('name')
        teachers = Teacher.objects.prefetch_related(
            Prefetch('subjects', queryset=queryset, to_attr='subject_list')
        )
        return teachers


def stu_teacher_salary_gt_alac(request):
    student_query = Student.objects.filter(subjects__teacher__salary__gt=1200000).only('name')
    students = list(student_query)
    return render(request, 'teachers/teacher_salary_gt_12l.html', {'students': students})


def teacher_search(request):
    if request.method == 'GET':
        teacher = request.GET.get('q')
        if not teacher:
            return redirect('/')
        teachers = Teacher.objects.filter(name__contains=teacher).prefetch_related(Prefetch('subjects__students', queryset=Student.objects.only('name'), to_attr='student_list'))
        teachers = list(teachers)
        return render(request, 'teachers/search.html', {'teachers': teachers})