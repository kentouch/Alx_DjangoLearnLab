from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required

# create views here

# list_of_books views
# let's create a view and add a permission decorator with a raise exception for restriction to the list of books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/home.html', {'list_books':books})

