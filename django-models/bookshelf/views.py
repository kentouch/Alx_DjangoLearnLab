from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignupView(CreateView):
    # uses the usercreationform as a form base for registration
    forms = UserCreationForm
    # After successful registration, there is a redirection to the login page
    success_url = reverse_lazy('login')
    # template name for the the registration form
    template_name = 'registr_templates/signup.html'
    
