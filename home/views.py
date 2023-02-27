from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView

# Create your views here.
class HomeView(TemplateView):
    template_name='home/index.html'

class LoginInterfaceView(LoginView):
    template_name='home/form.html'
#     model

class ProfileView(TemplateView):
    template_name='home/profile.html'

class MyLogoutView(LogoutView):
    next_page = '/login' 
    template_name = 'logout.html'


class SignupView(CreateView):
    model = User
    success_url='/'

 
    fields = ['username','first_name','last_name','email','password']