from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from artists.models import Artist
from artists.serializers import ArtistSerializer


class ArtistList(generics.ListCreateAPIView):
    """List with create view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []
