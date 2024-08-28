from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView
from .models import Library, Author, Librarian, Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            return messages.error('registration failed, try again')
    else:
        form = UserCreationForm
        return render(request, 'registration/signup.html', {'form': form})


#Implement Function-based View
def list_books(request):
    # retrieve all the books 
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/home.html', context)

#Implement Class-based View:
class LibraryDetailViews(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
    
    
