>>> from bookshelf.models import Book
>>> Book.objects.all
<bound method BaseManager.all of <django.db.models.manager.Manager object at 0x0000015B720FB290>>
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>