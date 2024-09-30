from django.urls import path
from . import views

urlpatterns = [
    # this path is used for the GET request for all books
    path('books/', views.BookListView.as_view()),
    # This path is used for the GET request for a single book
    path('books/<int:pk>/', views.BookDetailView.as_view()),
    # These three paths are used for the POST, PUT, and DELETE requests for books
    path('books/create/', views.BookCreateView.as_view()),
    path('books/update/', views.BookUpdateView.as_view()),
    path('books/delete/', views.BookDeleteView.as_view()),
]