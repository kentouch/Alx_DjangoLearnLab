from django.urls import path
from . import librarian_view
from .librarian_view import LibraryDetailViews
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', librarian_view.home, name='home'),
    path('register/', librarian_view.register, name='register' ),
    path('library/<int:pk>/', LibraryDetailViews.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'logout.html'), name='logout')
]