from django.db import models

# Create your models here.

# author model used for records about all authors in the database
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# book model used for records about all books in the database
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()