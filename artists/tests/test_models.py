"""Test artists models."""
from django.test import TestCase

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

    def test_verbose_names(self):
        """Test of verbose names."""
        self.assertEqual(Artist._meta.verbose_name, 'Artist')
        self.assertEqual(Artist._meta.verbose_name_plural, 'Artists')
