from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.
# Test Post model
class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='kentouch', password='2PACshakur.')
        #staff = self.client.force_login(user)
        Post.objects.create(title='Test Post', content='Test Content', author= user)

    def test_post_list(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')