"""Test serializers events."""
# Standard Library
import json

# Django
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# 3rd-party
from rest_framework import status
from rest_framework.test import APIRequestFactory

from artists.tests.factories import ArtistFactory
from events.models import Event
from events.serializers import EventListSerializer, EventCreateSerializer
from events.tests.factories import EventFactory


class TestEventSerializer(TestCase):
    """Test for Event serializers."""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.event = EventFactory()
        self.list_serializer = EventListSerializer(instance=self.event)
        self.create_serializer = EventCreateSerializer(instance=self.event)
        self.list_set_fields = [
            'name',
            'description',
            'localization_name',
            'longitude',
            'latitude',
            'artists',
            'date',
        ]
        self.create_set_fields = [
            'name',
            'description',
            'localization_name',
            'location',
            'artists',
            'date',
        ]

    def test_list_contains_expected_fields(self):
        """Test serializer list data fields."""
        data = self.list_serializer.data
        self.assertCountEqual(data.keys(), self.list_set_fields)

    def test_create_contains_expected_fields(self):
        """Test serializer create data fields."""
        data = self.create_serializer.data
        self.assertCountEqual(data.keys(), self.create_set_fields)

    def test_get_objects(self):
        """Test GET request status and data."""
        EventFactory()
        EventFactory()
        EventFactory()
        EventFactory()
        response = self.client.get(reverse('events_list'))
        events_query = Event.objects.all()
        serializer = EventListSerializer(events_query, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object_valid(self):
        """Test valid POST Event."""
        user = User.objects.create(
            username='test',
            password='1qaz@wsx'
        )
        artist = ArtistFactory()
        self.client.force_login(user)
        event = {
            "name": "213321",
            "description": "31231123",
            "localization_name": "1313132",
            "location": {
                "latitude": 12.1,
                "longitude": 24.4
            },
            "artists": [
                artist.id
            ],
            "date": "22-01-2021 23:49"
        }
        response = self.client.post(
            reverse('events_create'),
            data=json.dumps(event),
            content_type='application/json',
        )
        print(response.body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
