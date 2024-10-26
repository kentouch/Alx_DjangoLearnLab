# Extend Django’s UserCreationForm for the registration form to include additional fields like email.

from django.contrib.auth.forms import UserCreationForm
from django import forms  
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Develop a form for the Post model using Django’s ModelForm and implementing tag field
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    # Implement a condition for creating new tags that do not already exist in the database
    def tag(self):
        tags = forms.CharField(required=False)
        if tags not in Tag.objects.all():
            Tag.objects.create(name=tags)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
    

    # Ensure the form validates data properly and includes fields for title, content, 
    # automatically set author based on the logged-in user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.request.user

# Comment form for CRUD operations
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
