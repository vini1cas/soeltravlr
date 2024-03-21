from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Travel, Profile
from .forms import TravelForm
from django.urls import reverse_lazy

# Create your views here.
# def landing(request):
#     return render(request, 'home.html', {})

class Landing(ListView):
    model = Travel
    template_name = 'home.html'

class IntoTravel(DetailView):
    model = Travel
    template_name = 'travel_detail.html'

class MakeTravel(CreateView):
    model = Travel
    template_name = 'create_travel.html'
    form_class = TravelForm

class EditTravel(UpdateView):
    model = Travel
    template_name = 'edit_travel.html'
    form_class = TravelForm

class DeleteTravel(DeleteView):
    model = Travel
    template_name = 'delete_travel.html'
    success_url = reverse_lazy('landing')
