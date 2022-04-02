from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView, DeleteView, View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse_lazy('login')


class DashboardView(TemplateView):
    template_name = 'userprofile/dashboard.html'
    

class ProfileDetailView(TemplateView):
    template_name = 'userprofile/profile_detail.html'


class ProfileUpdateView(TemplateView):
    template_name = 'userprofile/profile_update.html'


class CompliantRegistrationView(TemplateView):
    template_name = 'userprofile/complaint_registration.html'


class ComplaintStatusView(TemplateView):
    template_name = 'userprofile/complaint_status.html'