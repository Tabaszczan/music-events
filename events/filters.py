import urllib

import requests
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import filters

from events.models import Event


class ClosestPlaces(filters.SearchFilter):
    search_title = 'Type location'
    search_description = 'Find events in 50km radius.'

    def filter_queryset(self, request, queryset, view):
        place_name = urllib.parse.quote_plus(request.query_params.get('search', ''))
        r = requests.get(
            f'https://maps.googleapis.com/maps/api/geocode/json?address={place_name}&key'
            f'={settings.GOOGLE_API_URL}'
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