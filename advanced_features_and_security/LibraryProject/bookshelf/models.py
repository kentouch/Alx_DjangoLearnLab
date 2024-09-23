from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

# Custom user model
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField()


class CustomUserManager(BaseUserManager):
# Create user with date of birth and profile photo
    def create_user(date_birth, profile_photo, *args, **kwargs):
        # Call create_user method from AbstractUser
        user = CustomUser.objects.create_user(*args, **kwargs)
        # Set date of birth and profile photo
        user.date_of_birth = date_birth
        user.profile_photo = profile_photo
        user.save()
        return user
        # Create superuser with date of birth and profile photo
    def create_superuser(date_birth, profile_photo, *args, **kwargs):
        # Call create_superuser method from AbstractUser
        user = CustomUser.objects.create_superuser(*args, **kwargs)
        # Set date of birth and profile photo
        user.date_of_birth = date_birth
        user.profile_photo = profile_photo
        user.save()
        return user

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    permission = ('can_view', 'can_create', 'can_edit', 'can_delete')

    def __str__(self):
        return self.title
