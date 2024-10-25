from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
# Test Post model
class PostModelTest(TestCase):
    def test_str_method(self):
        post = Post.objects.create(title='Test Post', content='Test Content')
        self.assertEqual(str(post), 'Test Post')