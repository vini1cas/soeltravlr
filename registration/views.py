from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import ProfileEditForm

# Create your views here.

class EditProfile(generic.UpdateView):
    form_class = ProfileEditForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('landing')

    def get_object(self):
        return self.request.user