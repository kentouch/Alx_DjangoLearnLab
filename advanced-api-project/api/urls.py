from django.urls import path
from . import views

urlpatterns = [
    # this path is used for the GET request for all books
    path('books/', views.BookListView.as_view(), name='book-list'),
    # This path is used for the GET request for a single book
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # These three paths are used for the POST, PUT, and DELETE requests for books
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),
]