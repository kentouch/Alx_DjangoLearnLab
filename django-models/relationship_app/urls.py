# urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from . import admin_view, librarian_view, member_view

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view.admin_only_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_only_view, name='librarian_view'),
    path('member/', member_view.member_only_view, name='member_view'),
]
