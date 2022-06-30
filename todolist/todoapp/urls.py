from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksView.as_view()),
    path('task/<int:pk>', TasksDetail.as_view(), name='task'),
]
