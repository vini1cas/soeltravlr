from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Travel, Profile
from .forms import TravelForm

# Create your views here.
# def landing(request):
#     return render(request, 'home.html', {})

class Landing(ListView):
    model = Travel
    template_name = 'home.html'

class IntoPost(DetailView):
    model = Travel
    template_name = 'post_detail.html'

class MakePost(CreateView):
    model = Travel
    template_name = 'create_post.html'
    form_class = TravelForm