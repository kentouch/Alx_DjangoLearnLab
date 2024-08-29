from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Library, Author, Librarian, Book, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# function test for admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


# admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin.html', {})