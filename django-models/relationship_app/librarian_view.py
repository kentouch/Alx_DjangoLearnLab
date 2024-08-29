from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Library, Author, Librarian, Book, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

# function test for admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


# function test for admin
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


# function test for admin
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# admin view
@user_passes_test(is_admin)
def admin_view(request):
    user = UserProfile.objects.all()
    if user.role == 'Admin':
        return render(request, 'admin.html', {})
    

# librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian.html', {})
    
# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member.html', {})

# register view
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
    
    
