from django.urls import path
from .views import teachers_gt_1

app_name = 'subjects'

urlpatterns = [
    path('teachers_gt_1/', teachers_gt_1, name='teachers_gt_1')
]