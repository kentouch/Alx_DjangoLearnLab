from django.db import models

# Create your models here.


#Author Model:
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

#Book Model:
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
#Library Model:


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#Librarian Model:
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library)