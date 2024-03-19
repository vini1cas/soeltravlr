
from django.urls import path
from .views import Landing, IntoPost, MakePost

urlpatterns = [
    path('', Landing.as_view(), name="landing"),
    path('post/<int:pk>', IntoPost.as_view(), name='post-detail'),
    path('make_post/', MakePost.as_view(), name="make-post")
]
