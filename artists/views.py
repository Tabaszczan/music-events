# 3rd-party
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

# Project
from artists.models import Artist
from artists.serializers import ArtistDetailSerializer
from artists.serializers import ArtistListSerializer


class ArtistList(generics.ListAPIView):
    """List view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['name']
    ordering_fields = ['name', 'genre']
    ordering = ['name']
    search_fields = ['name', 'genre']


class ArtistDetail(generics.RetrieveAPIView):
    """Detail view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
    permission_classes = []
    filter_backends = [SearchFilter]
    search_fields = ['get_participate_artists__name']


class ArtistCreate(generics.CreateAPIView):
    """Create view for Artist."""

    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer
    permission_classes = [IsAuthenticated]
