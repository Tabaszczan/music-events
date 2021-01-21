"""Test events models."""
from django.test import TestCase

from .factories import EventFactory
from ..models import  Event


class TestArtist(TestCase):
    """Test Artist model."""

    def test_string_representation(self):
        """Test if model has valid string representation."""
        event = EventFactory()
        self.assertEqual(
            str(event),
            f'Event {event.name}',
        )

    def test_verbose_names(self):
        """Test of verbose names."""
        self.assertEqual(Event._meta.verbose_name, 'Event')
        self.assertEqual(Event._meta.verbose_name_plural, 'Events')

    def test_longitude(self):
        """Test longitude property"""
        event = EventFactory()
        self.assertEqual(
            event.longitude,
            event.location.x,
        )
        self.assertEqual(
            event.longitude,
            Event.objects.get(id=event.id).longitude,
        )

    def test_latitude(self):
        """Test latitude property"""
        event = EventFactory()
        self.assertEqual(
            event.latitude,
            event.location.y,
        )
        self.assertEqual(
            event.latitude,
            Event.objects.get(id=event.id).latitude,
        )