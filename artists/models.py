"""Models artists."""
from django.db import models


# Create your models here.


class Artist(models.Model):
    """Artist model."""
    name = models.CharField('Artist name', max_length=255)
    genre = models.CharField('Music genre', max_length=255)

    @property
    def events(self):
        events = self.event_set.all().values_list('name', flat=True)
        return events

    @property
    def get_participate_artists(self):
        from artists.serializers import ArtistSerializer
        artists = []
        for item in self.event_set.all():
            serialize = ArtistSerializer(item.artists.exclude(id=self.id), many=True)
            artists.append(serialize.data)
        return artists

    def __str__(self):  # noqa: D105
        return f'Artist: {self.name}, Genre: {self.genre}'

    class Meta:  # noqa: D106
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'