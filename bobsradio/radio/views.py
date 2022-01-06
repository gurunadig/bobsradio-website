from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Artist, Podcast


def home(request):
    return render(request, 'radio/radio.html')   


def artist(request):
    artists = Artist.objects.all()
    context = {'artists':artists}
    return render(request, 'radio/artist.html', context)   


def about(request):
    return render(request, 'radio/about.html')   


def contact(request):
    return render(request, 'radio/contact.html')   


def radiotv(request):
    return render(request, 'radio/radiotv.html')   

def podcast(request):
    podcasts = Podcast.objects.all()
    context = {'podcasts':podcasts}
    return render(request, 'radio/podcast.html', context)   
