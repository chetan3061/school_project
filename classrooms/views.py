from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ClassRoom
from subjects.models import Subject
from django.db.models import Prefetch

# Create your views here.


class ClassRoomList(TemplateView):
    template_name = 'classrooms/classrooms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classroom_list = list(self.class_room_data())
        context['classroom_list'] = classroom_list
        return context

    def class_room_data(self):
        queryset = Subject.objects.only('name')
        classrooms = ClassRoom.objects.prefetch_related(
            Prefetch('subjects', queryset=queryset, to_attr='subject_list')
        )
        return classrooms



