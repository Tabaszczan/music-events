import datetime

from factory import post_generation
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyDecimal, FuzzyDate

from events.models import Event


class EventFactory(DjangoModelFactory):
    name = Faker('sentence')
    description = Faker('text')
    localization_name = Faker('city')
    longitude = FuzzyDecimal(-180, 180)
    latitude = FuzzyDecimal(-90, 90)
    date = FuzzyDate(
        datetime.date.today(),
        datetime.date(2121, 1, 1),
    )

    @post_generation
    def artists(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for artist in extracted:
                self.artists.add(artist)

    class Meta:  # noqa: D106
        model = Event
