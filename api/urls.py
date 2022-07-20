from django.urls import path
from .views import get_videos, add_video, get_charge
urlpatterns = [
    path('',get_videos, name='videos'),
    path('add/',add_video, name='addVideos'),
    path('charges/', get_charge, name='getCharge'),
]
