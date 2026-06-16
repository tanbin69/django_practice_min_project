from django.shortcuts import render
from datetime import datetime
from .models import Task

def home_view(request):
    # 1. Pull ALL tasks directly out of your SQLite Database
    database_tasks = Task.objects.all().order_by('-created_at')
    
    context = {
        'user_profile': {
            'name': 'tanbin',
            'role': 'Backend Engineering Intern',
        },
        'current_date': datetime.now(),
        'task_list': database_tasks, 
    }
    return render(request, 'home.html', context)
    
    context = {
        'user_profile': {
            'name': 'tanbin',
            'role': 'Backend Engineering Intern',
        },
        'current_date': datetime.now(),
        'task_list': mock_tasks,
    }
    return render(request, 'home.html', context)

def about_view(request):
    context = {
        'platform_specs': {
            'django_version': 5.0,
            'environment': 'isolated-dven',
        }
    }
    return render(request, 'about.html', context)
