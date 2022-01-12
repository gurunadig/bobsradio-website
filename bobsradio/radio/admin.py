from django.contrib import admin
from .models import Artist, Podcast, Radiolink

admin.site.register(Artist)
admin.site.register(Podcast)
admin.site.register(Radiolink)
