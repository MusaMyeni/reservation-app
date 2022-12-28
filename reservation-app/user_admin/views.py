from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyAuthenticationForm

# Create your views here.
class MyLoginView(LoginView):
    template_name = "login.html"
    authentication_form=MyAuthenticationForm

class MyLogoutView(LogoutView):
    template_name = "logout.html"
    authentication_form=MyAuthenticationForm
