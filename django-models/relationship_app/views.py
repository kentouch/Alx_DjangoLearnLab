from django.shortcuts import render, redirect
from django.views.generic import DetailView
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
        return render(request, 'register.html', {'form': form})


#Implement Function-based View
def home(request):
    # retrieve all the books 
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'home.html', context)

#Implement Class-based View:
class LibraryDetailViews(DetailView):
    model = Library
    template_name = 'library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()
        return context
    
    
