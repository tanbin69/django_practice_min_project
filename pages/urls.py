from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_route'),
    path('about/', views.about_view, name='about_route'),
    
    # URL patterns that pass the specific Task ID database key to Python
    path('complete/<int:task_id>/', views.complete_task_view, name='complete_task_route'),
    path('delete/<int:task_id>/', views.delete_task_view, name='delete_task_route'),
]