"""Urls events."""
# Django
from django.urls import path

# Local
from artists.views import ArtistList
from .views import api_root, EventList

urlpatterns = [
    path('', api_root),
    path('events/', EventList.as_view(), name='events_list'),
    path('artist/', ArtistList.as_view(), name='artist_list')
]