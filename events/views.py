from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from events.models import Event
from events.serializers import EventSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """View for links to endpoints."""
    return Response({
        'events': reverse('events_list', request=request, format=format),
        'artist': reverse('artist_list', request=request, format=format)
    })


class EventList(generics.ListCreateAPIView):
    """List with create view for events."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []
