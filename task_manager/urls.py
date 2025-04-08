from django.urls import path
from task_manager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project_v', views.ProjectViewSet, basename='projects_v')
router.register('option', views.ProjectViewSetOptional, basename='Optional')
router.register('task', views.TaskViewSet, basename='task')
urlpatterns = [
                  path('', views.FirstAPIView.as_view(), name='first'),
                  path('project/', views.ProjectAPIView.as_view(), name='project_list'),
                  path('project/<int:pk>/', views.ProjectAPIView.as_view(), name='project_detail')
              ] + router.urls
