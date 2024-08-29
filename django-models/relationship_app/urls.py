# urls.py

from django.urls import path
from views import LibraryView
from . import admin_view, librarian_view, member_view, views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('library/', LibraryView.as_view(), name='library_detail'),
    path('admin/', admin_view.admin_only_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_only_view, name='librarian_view'),
    path('member/', member_view.member_only_view, name='member_view'),
]
