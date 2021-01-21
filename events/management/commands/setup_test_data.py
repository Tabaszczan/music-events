"""Custom command file."""
# Standard Library
import random

# Django
from django.core.management.base import BaseCommand
from django.db import transaction

# Project
from artists.models import Artist
from artists.tests.factories import ArtistFactory
from events.models import Event
from events.tests.factories import EventFactory

NUM_ARTISTS = 50
NUM_EVENTS = 10
ARTIST_PER_EVENT = 5


class Command(BaseCommand):  # noqa: D101
    help = 'Generates test data'

    @transaction.atomic
    def handle(self, *args, **kwargs):  # noqa: D102
        self.stdout.write('Deleting old data...')
        models = [Artist, Event]
        for m in models:
            m.objects.all().delete()

        self.stdout.write('Creating new data...')
        artists = []
        for _ in range(NUM_ARTISTS):
            artist = ArtistFactory()
            artists.append(artist)

        for _ in range(NUM_EVENTS):
            event = EventFactory()
            artist = random.choices(
                artists,
                k=ARTIST_PER_EVENT,
            )
            event.artists.add(*artist)
