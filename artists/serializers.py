"""Serializers artists."""
# 3rd-party
from rest_framework import serializers

# Local
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):
    """Serializer for Artist list model."""

    class Meta:  # noqa: D106
        model = Artist
        fields = ['name', 'genre', 'events']


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist participate."""

    class Meta:  # noqa: D106
        model = Artist
        fields = ['name', 'genre']


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Serializer for Artist detail model."""

    class Meta:  # noqa: D106
        model = Artist
        fields = ['name', 'genre', 'get_participate_artists']
