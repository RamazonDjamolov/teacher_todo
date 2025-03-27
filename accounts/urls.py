from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login')
]
