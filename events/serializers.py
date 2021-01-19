from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer Events model."""

    class Meta:
        model = Event
        fields = ['name', 'description', 'localization_name', 'coordinates', 'artists']

