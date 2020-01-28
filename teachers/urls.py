from django.urls import path
from .views import TeacherList, stu_teacher_salary_gt_alac, teacher_search

app_name = 'teacher'
urlpatterns = [
    path('list/', TeacherList.as_view(), name='list'),
    path('teachers_gt_12l/', stu_teacher_salary_gt_alac, name='teacher_salary_gt_12l'),
    path('search/', teacher_search, name='search')
]