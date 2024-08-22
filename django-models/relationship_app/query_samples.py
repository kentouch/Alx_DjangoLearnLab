from .models import Book, Library, Librarian
# Queries for the database

# Query all books by a specific author
Book.objects.filter(author='Joe different')

# List all books in a library.
library= Library.objects.get(name=library_name)
library.books.all()
# Retrieve the librarian for a library.
Librarian.objects.get(library= 'Saint Lorence')