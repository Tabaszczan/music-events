"""Urls events."""
# Django
from django.urls import path

# Project
from artists.views import ArtistCreate
from artists.views import ArtistDetail
from artists.views import ArtistList

# Local
from .views import EventCreate
from .views import EventList
from .views import api_root

urlpatterns = [
    path('', api_root),
    path('events/', EventList.as_view(), name='events_list'),
    path('events/create/', EventCreate.as_view(), name='events_create'),
    path('artist/', ArtistList.as_view(), name='artist_list'),
    path('artist/<int:pk>/', ArtistDetail.as_view(), name='artist_detail'),
    path('artist/create/', ArtistCreate.as_view(), name='artist_create'),

]
