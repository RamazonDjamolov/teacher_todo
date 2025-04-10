from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('token-login', views.LoginWithTokenViewSet, basename='login_token')

urlpatterns = [
                  path('login/', views.LoginAPIView.as_view(), name='login'),
                  path('logout/', views.LogoutAPIView.as_view(), name='logout'),
                  path('session/', views.SessionAPIView.as_view(), name='session'),
                  path('register/', views.RegisterAPIView.as_view(), name='register'),
              ] + router.urls
