from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Custom user model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField()
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
