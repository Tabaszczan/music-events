"""Events filters."""
# Standard Library
import urllib

# Django
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

# 3rd-party
import requests
from rest_framework import filters


class ClosestPlaces(filters.SearchFilter):
    """Custom search filter for closest events."""

    search_title = 'Type location'
    search_description = 'Find events in 50km radius.'

    def filter_queryset(self, request, queryset, view):
        """Return events in 50km radius form place typed in search."""
        place_name = urllib.parse.quote_plus(request.query_params.get('search', ''))
        r = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key'
            f'={settings.GOOGLE_API_URL}',
        )
        if r.status_code == 200:
            lat = r.json()['results'][0]['geometry']['location']['lat']
            lng = r.json()['results'][0]['geometry']['location']['lng']
            events_in_radius = queryset.filter(
                location__distance_lt=(
                    Point(lat, lng),
                    Distance(km=50),
                ),
            )
            return events_in_radius
        return queryset
