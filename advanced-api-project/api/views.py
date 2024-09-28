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
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

# Construct a view for updating books through the API
"""class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        serializer.save()"""

# Construct a view for detailing books through the API

class BookDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

