from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker

from artists.tests.factories import ArtistFactory
from events.models import Event


class EventFactory(DjangoModelFactory):

    name = Faker()
    description = Faker('text')
    localization_name = Faker()
    coordinates = Faker()
    artists = SubFactory(ArtistFactory)
    date = Faker()

    class Meta:  # noqa: D106
        model = Event