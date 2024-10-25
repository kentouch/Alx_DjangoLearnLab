from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.index, name='index'),
    path('about/', views.HomeView.about, name='about'),
    path('login/', views.HomeView.login, name='login'),
    path('logout', views.HomeView.logout, name='logout'),
    path('register/', views.HomeView.register, name='register'),
    path('profile/', views.HomeView.profile, name='profile'),
]