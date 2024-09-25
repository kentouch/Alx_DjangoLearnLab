# let's make a url that directs to the view

from django.urls import path
from .views import BookList

urlpatterns = [
    path('api/books/', BookList.as_view(), name= 'BookListView')
]