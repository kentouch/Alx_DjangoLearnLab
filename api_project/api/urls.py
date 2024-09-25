# let's make a url that directs to the view

from django.urls import path
from .views import Booklist

urlpatterns = [
    path('api/books/', Booklist.as_view(), name= 'BookListView')
]