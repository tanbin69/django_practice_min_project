from django.shortcuts import render, redirect
from datetime import datetime
from .models import Task

def home_view(request):
    # 1. Handle New Task Submission (Form Creation)
    if request.method == "POST":
        task_title = request.POST.get("title")
        task_priority = request.POST.get("priority")
        
        if task_title:  # Security check to ensure it isn't empty
            Task.objects.create(title=task_title, priority=task_priority)
        
        return redirect('home_route')  # Refresh the page to show the new item

    # 2. Display All Live Tasks
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

# 3. New Dynamic Action: Mark a task as Complete
def complete_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()  # Saves changes back into db.sqlite3
    return redirect('home_route')

# 4. New Dynamic Action: Delete a task permanently
def delete_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()  # Removes item from db.sqlite3
    return redirect('home_route')

def about_view(request):
    context = {
        'platform_specs': {
            'django_version': 5.0,
            'environment': 'isolated-dven',
        }
    }
    return render(request, 'about.html', context)