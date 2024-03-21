
from django.urls import path
from .views import Landing, IntoTravel, MakeTravel, EditTravel, DeleteTravel

urlpatterns = [
    path('', Landing.as_view(), name="landing"),
    path('travel/<int:pk>', IntoTravel.as_view(), name="travel-detail"),
    path('make_travel/', MakeTravel.as_view(), name="make-travel"),
    path('travel/<int:pk>/edit', EditTravel.as_view(), name="edit-travel"),
    path('travel/<int:pk>/delete', DeleteTravel.as_view(), name="delete-travel"),
]
