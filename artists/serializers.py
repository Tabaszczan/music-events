from rest_framework import serializers

from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer):
    """Serializer for Artist list model."""

    class Meta:
        model = Artist
        fields = ['name', 'genre', 'events']


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist participate."""

    class Meta:
        model = Artist
        fields = ['name', 'genre']


class ArtistDetailSerializer(serializers.ModelSerializer):
    """Serializer for Artist detail model."""

    class Meta:
        model = Artist
        fields = ['name', 'genre', 'get_participate_artists']
