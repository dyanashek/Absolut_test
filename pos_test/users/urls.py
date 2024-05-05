from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_or_signup, name = 'login_or_signup'),
] 