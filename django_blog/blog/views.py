from django.shortcuts import render
from .models import Post
from .forms import RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# let's import auhtentication classes

# Create your views here.
# Utilize Django’s built-in authentication views and forms to handle user login and logout. 
# For registration and profile management, custom views will be created.
class HomeView:
    # index for the home page
    def index(request):
        return render(request, 'blog/index.html')
    # about for the about page
    def about(request):
        return render(request, 'blog/about.html')
    
    # login view
    def login(request):
        return render(request, 'blog/login.html')
    
    # logout view
    def logout(request):
        return render(request, 'blog/logout.html')
    
    # register view
    def register(request):
        return render(request, 'blog/register.html')
    
    # profile view
    # Develop a view that allows authenticated users to view and edit their profile details.
    # This view should handle POST requests to update user information.
    # It should also handle GET requests to display the user profile.
    def profile(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'blog/profile.html')
        return render(request, 'blog/profile.html')
    
# use class based views to handle CRUD operations
# ListView to display all blog posts.
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

# Detail View to display a specific blog post.
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html' 

# Create View to create a new blog post.
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

# Update View to update an existing blog post.
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    # test if the user is the author
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

# Delete View to delete an existing blog post.
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    # test if the user is the author
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user