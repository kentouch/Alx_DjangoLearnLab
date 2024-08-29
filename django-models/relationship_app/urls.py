# urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register
from . import admin_view, librarian_view, member_view

urlpatterns = [

    path('', list_books, name='list_books'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view.admin_only_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_only_view, name='librarian_view'),
    path('member/', member_view.member_only_view, name='member_view'),
]
