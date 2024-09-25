from django.shortcuts import render
from api.serializers import BookSerializer
from rest_framework import generics
from .models import Book

# Create your views here.
class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer