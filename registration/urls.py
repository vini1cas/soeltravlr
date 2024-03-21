from django.urls import path
from .views import EditProfile

urlpatterns = [
    path('profile-edit/', EditProfile.as_view(), name='edit-profile')
]