from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from artists.models import Artist
from artists.serializers import ArtistSerializer
from rest_framework.permissions import IsAuthenticated


class ArtistList(generics.ListAPIView):
    """List view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = []


class ArtistCreate(generics.CreateAPIView):
    """Create view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]
