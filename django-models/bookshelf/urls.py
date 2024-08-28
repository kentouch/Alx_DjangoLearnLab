from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# Outline the paths needed below

Urlpatterns = [

    path('/login', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('/logout', LogoutView.as_view(), name='logout')
]