from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from django_filters import rest_framework
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
# This view is used to retrieve all books in the database
class BookListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # filtering book by title, author and publication_year
    filter_backends = [rest_framework.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

# Construct a view for creating books through the API
# Implement a set of generic views for the Book model to handle CRUD operations. This includes:
# A ListView for retrieving all books.
class BookDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A DetailView for retrieving a single book by ID.
class BookCreateView(generics.CreateAPIView):
    # permissions = [IsAuthenticatedOrReadOnly, IsAdminUser]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A CreateView for adding a new book.
class BookUpdateView(generics.UpdateAPIView):
    permissions = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# An UpdateView for modifying an existing book.
class BookDeleteView(generics.DestroyAPIView):
    permissions = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# A DeleteView for removing a book.
