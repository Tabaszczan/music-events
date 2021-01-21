from django.test import TestCase

from events.tests.factories import EventFactory
from ..tests.factories import ArtistFactory


class TestArtist(TestCase):
    """Test Artist model."""
    def setUp(self) -> None:
        self.artist = ArtistFactory()


    def test_string_representation(self):
        """Test if model has valid string representation."""
        self.assertEqual(
            str(self.artist),
            f'Artist: {self.artist.name}, Genre: {self.artist.genre}'
        )

    def test_events(self):
        """Test artist events list."""
        event = EventFactory(artist=self.artist)
        self.assertEqual(
            event.values_list('name', flat=True),
            self.artist.events
        )
