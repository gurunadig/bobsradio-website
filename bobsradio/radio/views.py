from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Artist, Podcast, Radiolink


def home(request):
    artists = Artist.objects.all()[0:3]
    radiolinks = Radiolink.objects.all()
    context = {'artists':artists, 'radiolinks':radiolinks}
    return render(request, 'radio/radio.html', context)   


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

def artistdetails(request, pk):
    artistdetails = Artist.objects.filter(id=pk)
    context = {'artistdetails':artistdetails}
    return render(request, 'radio/ArtistDetails.html', context)   