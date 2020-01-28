from django.urls import path
from .views import ClassRoomList

app_name = 'classroom'
urlpatterns = [
    path('list/', ClassRoomList.as_view(), name='list')
]