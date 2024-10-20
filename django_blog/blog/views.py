from django.shortcuts import render

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
    def profile(request):
        return render(request, 'blog/profile.html')
    
