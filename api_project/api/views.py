from django.shortcuts import render
from api.serializers import BookSerializer
from rest_framework import generics, viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    # these permissions are for the admin we start by permi
    permission_classes = [IsAuthenticated]
    permissions = [IsAdminUser]
    # queryset = Book.objects.all()
    queryset = Book.objects.all()
    serializer_class = BookSerializer