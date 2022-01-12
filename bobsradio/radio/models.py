from django.db import models
from ckeditor.fields import RichTextField

class Artist(models.Model):
    artist_name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(default="400-200.png", null=False, blank=True)
    artist_bio = RichTextField(blank=True, null=True)
    genre = models.CharField(max_length=100, blank=False, null=False)
    year_of_inception = models.DateTimeField(blank=False, null=False)
    albums = RichTextField(blank=True, null=True)
    songs_trivia = RichTextField(blank=True, null=True)
    anniversary_date = models.CharField(max_length=50, null=False, blank=False)
    facebook_url = models.TextField()
    instagram_url = models.TextField() 

    def __str__(self):
        return self.artist_name


class Podcast(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = RichTextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title



class Radiolink(models.Model):
    url = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.url
