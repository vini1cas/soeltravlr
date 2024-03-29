from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Travel, Profile
from .forms import TravelForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def landing(request):
#     return render(request, 'home.html', {})

class Landing(ListView):
    model = Travel
    template_name = 'home.html'

class IntoProfile(DetailView):
    model = Profile 
    template_name = 'profile.html'

    def get_meta_data (self, *args, **kwargs):
        meta = super(IntoProfile, self).get_context_data(*args, **kwargs)

        user = get_object_or_404(Profile, id=self.kwargs['pk'])
        meta['user'] = user
        return meta

class ProfileEdit(generic.UpdateView):
    model = Profile
    template_name = 'edit-profile.html'
    fields = ['bio', 'pic','social_media', 'website']
    success_url = reverse_lazy('profile')

class IntoTravel(DetailView):
    model = Travel
    template_name = 'travel_detail.html'

    def get_meta_data (self, *args, **kwargs):
        meta = super(InfoTravel, self).get_context_data(*args, **kwargs)

        info = get_object_or_404(Travel, id=self.kwargs['pk'])
        total_likes = info.likes()

        liked = False
        if info.like.filter(id=self.request.user.id):
            liked = True

        meta["total_likes"] = total_likes
        meta["liked"] = liked
        return meta

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

def LikeTravel(request, pk):
    travel = get_object_or_404(Travel, id=request.POST.get('travel_id'))
    liked = False
    if travel.like.filter(id=request.user.id).exists():
        travel.like.remove(request.user)
        liked = False
    else:
        travel.like.add(request.user)
        liked = True
        return HttpResponseRedirect(reverse('travel-detail', args=[str(pk)]))

