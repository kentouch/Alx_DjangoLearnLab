from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library, Author, Librarian

# Create your views here.

#Implement Function-based View
def book_list(request):
    # retrieve all the books 
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

#Implement Class-based View:
class LibraryDetailViews(DetailView):
    model = Library
    template_name = 'library.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
    
    
