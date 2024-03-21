from django.urls import path
from .views import UserSignUp

urlpatterns = [
    path('sign_up/', UserSignUp.as_view(), name='sign-up')
]