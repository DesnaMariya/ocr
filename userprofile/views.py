from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView, DeleteView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = UserCreationForm
    # fields = ['email', 'username', 'password1', 'password2']
