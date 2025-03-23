from django.urls import path
from task_manager import views

urlpatterns = [
    path('', views.FirstAPIView.as_view(), name='first'),
    path('project', views.ProjectAPIView.as_view(), name='project_list')
]
