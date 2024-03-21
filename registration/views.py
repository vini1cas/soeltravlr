from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, ProfileEditForm

# Create your views here.

class UserSignUp(generic.CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

class EditProfile(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('landing')

    def get_object(self):
        return self.request.user