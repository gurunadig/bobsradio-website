from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artist', views.artist, name='artist'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('radiotv', views.radiotv, name='radiotv'),
    path('podcast', views.podcast, name='podcast'),
    path('ArtistDetails/<str:pk>', views.artistdetails, name='artistdetails'),
]
