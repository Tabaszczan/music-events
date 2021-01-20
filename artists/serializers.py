from rest_framework import serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist model."""
    class Meta:
        model = Artist
        fields = ['name', 'genre']