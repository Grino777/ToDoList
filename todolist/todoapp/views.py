from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Task

# Create your views here.

class TaskView(ListView):
    model = Task
    template_name = 'todoapp/index.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'todoapp/detail_view.html'
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('all_tasks')
    template_name = 'todoapp/task_form.html'