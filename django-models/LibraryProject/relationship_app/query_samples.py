from .models import Book, Library, Librarian

# Query all books by a specific author.
book = Book.objects.all()

# List all books in a library.
books = Library.objects.get(book = 'Easy')

# Retrieve the librarian for a library.
librarian = Librarian.objects.get(library = 'Read and feel')