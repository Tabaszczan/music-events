"""Artists factories."""
# 3rd-party
from factory.django import DjangoModelFactory
from factory.faker import Faker

# Project
from artists.models import Artist


class ArtistFactory(DjangoModelFactory):
    """Artist factory."""

    name = Faker('name')
    genre = Faker('sentence')

    class Meta:  # noqa: D106
        model = Artist
