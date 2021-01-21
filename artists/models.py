"""Models artists."""
# Django
from django.db import models


class Artist(models.Model):
    """Artist model."""

    name = models.CharField('Artist name', max_length=255)
    genre = models.CharField('Music genre', max_length=255)

    @property
    def events(self):
        """Get artist events list."""
        events = self.event_set.all().values_list('name', flat=True)
        return events

    @property
    def get_participate_artists(self):
        """Get artists that participate in same events."""
        # Local
        from .serializers import ArtistSerializer
        x = None
        for item in self.event_set.all():
            if x:
                x |= item.artists.exclude(id=self.id)
            else:
                x = item.artists.exclude(id=self.id)
        serialize = ArtistSerializer(x.distinct(), many=True)
        return serialize.data

    def __str__(self):  # noqa: D105
        return f'Artist: {self.name}, Genre: {self.genre}'

    class Meta:  # noqa: D106
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'
