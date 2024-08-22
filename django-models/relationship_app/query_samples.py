from .models import Book, Library, Librarian, Author
# Queries for the database

# Query all books by a specific author
author = Author.objects.get(author='Joe different')
Book.objects.filter(author= author)
# List all books in a library.
library_name= Library.objects.get(name=library_name)
library_name.books.all()
# Retrieve the librarian for a library.
Librarian.objects.get(library= library_name)