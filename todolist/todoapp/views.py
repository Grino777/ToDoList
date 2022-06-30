from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Tasks

# Create your views here.

class TasksView(ListView):
    model = Tasks
    template_name = 'todoapp/index.html'
    context_object_name = 'tasks'

class TasksDetail(DetailView):
    model = Tasks
    template_name = 'todoapp/detail_view.html'
    context_object_name = 'task'

class CreateTask(CreateView):
    pass