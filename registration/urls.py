from django.urls import path
from .views import UserSignUp, EditProfile

urlpatterns = [
    path('sign-up/', UserSignUp.as_view(), name='sign-up'),
    path('profile-edit/', EditProfile.as_view(), name='edit-profile')
]