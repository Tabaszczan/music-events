from django.test import TestCase

from events.models import Event
from events.tests.factories import EventFactory
from ..models import Artist
from ..tests.factories import ArtistFactory


class TestArtist(TestCase):
    """Test Artist model."""

    def test_string_representation(self):
        """Test if model has valid string representation."""
        artist = ArtistFactory()
        self.assertEqual(
            str(artist),
            f'Artist: {artist.name}, Genre: {artist.genre}'
        )

    def test_events(self):
        """Test artist events list."""
        artist = ArtistFactory()
        event = EventFactory(artists__in=artist)
        self.assertEqual(
            event.name,
            Artist.objects.first().events,
        )
