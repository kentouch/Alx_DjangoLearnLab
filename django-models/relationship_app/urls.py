from django.urls import path
from .views import list_books, LibraryDetailViews
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailViews.as_view(), name='library_detail'),
    path('/login', LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('/logout', LogoutView.as_view(), name='logout')
]