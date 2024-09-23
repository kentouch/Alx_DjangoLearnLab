from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from bookshelf.models import CustomUser 

# Create your models here.


# first step: Extend the User Model with a UserProfile

# user profile model
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    ROLE_CHOICES = [
    ('Admin', 'ADMIN'),
    ('librarian', 'LIBRARIAN'),
    ('Member','MEMBER')
]
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='admin')


# Signal to create or update UserProfile when CustomUser is saved
@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()

# Author model
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

# Library model
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name 

# Librarian model
class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name