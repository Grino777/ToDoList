from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskView.as_view(), name='all_tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
]
