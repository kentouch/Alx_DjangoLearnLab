# Extend Django’s UserCreationForm for the registration form to include additional fields like email.

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Develop a form for the Post model using Django’s ModelForm 
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    

    # Ensure the form validates data properly and includes fields for title, content, 
    # automatically set author based on the logged-in user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].initial = self.request.user
