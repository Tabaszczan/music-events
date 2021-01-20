"""Urls events."""
# Django
from django.urls import path

# Local
from artists.views import ArtistList, ArtistCreate
from .views import api_root, EventList, EventCreate

urlpatterns = [
    path('', api_root),
    path('events/', EventList.as_view(), name='events_list'),
    path('events/create', EventCreate.as_view(), name='events_create'),
    path('artist/', ArtistList.as_view(), name='artist_list'),
    path('artist/create', ArtistCreate.as_view(), name='artist_create'),
]