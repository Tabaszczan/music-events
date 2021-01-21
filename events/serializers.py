"""Events serializers."""
# 3rd-party
from django.contrib.gis.geos import Point
from drf_extra_fields.geo_fields import PointField
from rest_framework import serializers

# Local
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    """Serializer Events model on list view."""

    date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    artists = serializers.StringRelatedField(many=True)

    class Meta:  # noqa: D106
        model = Event
        fields = [
            'name',
            'description',
            'localization_name',
            'longitude',
            'latitude',
            'artists',
            'date',
        ]


class EventCreateSerializer(serializers.ModelSerializer):
    """Serializer Events model on create view."""

    date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    location = PointField()

    class Meta:  # noqa: D106
        model = Event
        fields = [
            'name',
            'description',
            'localization_name',
            'location',
            'artists',
            'date',
        ]
