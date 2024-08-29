# admin_view.py

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .test_func import is_admin, is_member, is_librarian  # Assuming utils.py is in the same directory
from .models import Library, Book, Librarian
from django.views.generic.detail import DetailView

# create your views here

# list_of_books views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'list_books':books})


#class based view
class LibraryView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['list_books'] = Library.objects.filter(books=self.objects.books)

        return context
    


@user_passes_test(is_admin)
def admin_only_view(request):
    return HttpResponse("This view is for Admins only.")

@user_passes_test(is_member)
def member_only_view(request):
    return HttpResponse("This view is for Members only.")


@user_passes_test(is_librarian)
def librarian_only_view(request):
    return HttpResponse("This view is for Librarians only.")
