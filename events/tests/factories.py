"""Events factories."""
# Standard Library
import datetime

# Django
from django.contrib.gis.geos import Point

# 3rd-party
from factory import post_generation
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyDateTime
from factory.fuzzy import FuzzyFloat
from pytz import UTC

# Local
from ..models import Event


class EventFactory(DjangoModelFactory):
    """Event factory."""

    name = Faker('sentence')
    description = Faker('text')
    localization_name = Faker('city')
    date = FuzzyDateTime(
        datetime.datetime(2021, 1, 1, tzinfo=UTC),
        datetime.datetime(2121, 1, 1, tzinfo=UTC),
    )

    @post_generation
    def artists(self, create, extracted, **kwargs):
        """Generate artists relation."""
        if not create:
            return

        if extracted:
            for artist in extracted:
                self.artists.add(artist)

    @post_generation
    def location(self, create, extracted, **kwargs):
        """Generate random location."""
        if create:
            self.location = Point(FuzzyFloat(-180, 180).fuzz(), FuzzyFloat(-90, 90).fuzz())

    class Meta:  # noqa: D106
        model = Event
