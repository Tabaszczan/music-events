from factory.django import DjangoModelFactory
from factory.faker import Faker
from artists.models import Artist


class ArtistFactory(DjangoModelFactory):

    name = Faker('name')
    genre = Faker('sentence')

    class Meta:  # noqa: D106
        model = Artist