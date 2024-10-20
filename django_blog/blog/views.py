from django.shortcuts import render
from django.forms import RegisterForm
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
    def login(request):
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
    
