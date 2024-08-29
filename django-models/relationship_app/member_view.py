from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Library, Author, Librarian, Book, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


# function test for admin
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member.html', {})