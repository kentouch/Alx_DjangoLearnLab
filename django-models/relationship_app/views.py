from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import Library, Author, Librarian, Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignupView(CreateView):
    # uses the usercreationform as a form base for registration
    forms = UserCreationForm
    # After successful registration, there is a redirection to the login page
    success_url = reverse_lazy('login')
    # template name for the the registration form
    template_name = 'registr_templates/signup.html'

#Implement Function-based View
def list_books(request):
    # retrieve all the books 
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

#Implement Class-based View:
class LibraryDetailViews(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
    
    
