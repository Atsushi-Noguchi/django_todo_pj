from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from todoapp.models import Task

class TaskList(ListView):
    model = Task
