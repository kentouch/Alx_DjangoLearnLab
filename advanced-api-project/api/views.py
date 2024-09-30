from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from serializers import BookSerializer

# Create your views here.
# This view is used to retrieve all books in the database
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Construct a view for creating books through the API
# Implement a set of generic views for the Book model to handle CRUD operations. This includes:
# A ListView for retrieving all books.
class BookDetailView(generics.DetailApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A DetailView for retrieving a single book by ID.
class BookCreateView(generics.CreateApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A CreateView for adding a new book.
class BookUpdateView(generics.UpdateApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# An UpdateView for modifying an existing book.
class BookDeleteView(generics.DeleteApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A DeleteView for removing a book.
