from django.db import models

# Create your models here.

# author model : name(Char)
class Author(models.Model):
    name = models.CharField(max_length=200)

# Book model: title(Char), author(ForeignKey)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Library model: name(Char), books(ManytoManyField)
class Library(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField(Book)

# Librarian model: name(Char), library(OnetoOneField)
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)