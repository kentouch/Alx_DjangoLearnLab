from django.urls import path
from .views import list_books, LibraryDetailViews

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailViews.as_view(), name='library_detail'),
]