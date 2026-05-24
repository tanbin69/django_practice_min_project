from django.shortcuts import render
from datetime import datetime

def home_view(request):
    # Dummy mock database objects to pass to templates
    mock_tasks = [
        {'title': 'Configure Django TEMPLATES directory path settings', 'priority': 'High', 'is_completed': True},
        {'title': 'Fix Git Bash path environmental variables crash', 'priority': 'High', 'is_completed': True},
        {'title': 'Build out template inheritance structures', 'priority': 'Medium', 'is_completed': False},
        {'title': 'Connect dynamic SQLite Database layer models', 'priority': 'Low', 'is_completed': False},
    ]
    
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
