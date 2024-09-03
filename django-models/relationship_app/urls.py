# urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import admin_view, librarian_view, member_view

urlpatterns = [

    path('register/', views.register, name='register'),
    path('', views.list_books, name='list_books'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('change_book/', views.change_book, name='change_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name='logout'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view.admin_only_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_only_view, name='librarian_view'),
    path('member/', member_view.member_only_view, name='member_view'),
]
