"""Test serializers events."""
# Standard Library
import json

# Django
from django.test import TestCase
from django.urls import reverse

# 3rd-party
from rest_framework import status
from rest_framework.test import APIRequestFactory

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
            'longitude',
            'latitude',
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
        response = self.client.get(reverse('cars_list'))
        cars_query = Event.objects.all()
        serializer = EventListSerializer(cars_query, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object_valid(self):
        """Test valid POST Event."""
        event = {
            'name': 'TEST',
            'description': 'DESCRIPTION DEST',
            'localization_name': 'LOCALIZATION TEST',
            'longitude': 12.0,
            'latitude': 14.0,
            'date': '01-01-2021 11:00',
        }
        response = self.client.post(
            reverse('events_create'),
            data=json.dumps(event),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
