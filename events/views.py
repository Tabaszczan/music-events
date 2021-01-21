# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from events.filters import ClosestPlaces
from events.models import Event
from events.serializers import EventListSerializer, EventCreateSerializer
import requests
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point


@api_view(['GET'])
def api_root(request, format=None):
    """View for links to endpoints."""
    return Response({
        'events_list': reverse('events_list', request=request, format=format),
        'events_create': reverse('events_create', request=request, format=format),
        'artist_list': reverse('artist_list', request=request, format=format),
        'artist_create': reverse('artist_create', request=request, format=format)
    })


class EventList(generics.ListAPIView):
    """List view for events."""

    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    permission_classes = []
    filter_backends = [ClosestPlaces]
    search_fields = ['']


class EventCreate(generics.CreateAPIView):
    """Create view for events."""
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAuthenticated]

