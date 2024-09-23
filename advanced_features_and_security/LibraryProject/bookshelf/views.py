from django.shortcuts import render
from .models import Book

# create views here

# list_of_books views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/home.html', {'list_books':books})

