
from  .models import Book, CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

# register the custom user model with the admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'role')
    search_fields = ('username', 'role')


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)