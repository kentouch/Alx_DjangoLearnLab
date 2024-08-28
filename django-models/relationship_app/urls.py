from django.urls import path
from . import views
from .views import LibraryDetailViews
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.list_books, name='home'),
    path('register/', views.register, name='register' ),
    path('library/<int:pk>/', LibraryDetailViews.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name= 'registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'registration/login.html'), name='logout')
]