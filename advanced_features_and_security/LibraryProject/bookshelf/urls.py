from django.urls import path
from .views import book_list, example_form


# Outline the paths needed below

Urlpatterns = [
    path('', book_list, name='list_of_books'),
    path('contact/', example_form, name='form_example'),
]