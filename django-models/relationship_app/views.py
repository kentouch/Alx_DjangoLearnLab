# admin_view.py

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .test_func import is_admin, is_member, is_librarian  # Assuming utils.py is in the same directory
from .models import Library, Book, Librarian
from django.views.generic.detail import DetailView

# create your views here

# list_of_books views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/home.html', {'list_books':books})


# LibraryDetailViewclass based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['list_books'] = Library.objects.filter(books=self.objects.books)

        return context
    

# register view
def register(request):
    # if request method is equal POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user) # log the user in after successful registration
            redirect('home')
    else:
        # if the form is not submitted
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form' : form})

        


@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("This view is for Admins only.")

@user_passes_test(is_member)
def member_only_view(request):
    return HttpResponse("This view is for Members only.")


@user_passes_test(is_librarian)
def librarian_only_view(request):
    return HttpResponse("This view is for Librarians only.")
