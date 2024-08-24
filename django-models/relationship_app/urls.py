from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
]