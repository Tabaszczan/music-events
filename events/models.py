"""Models events."""
# Create your models here.
from artists.models import Artist
from django.db import models


class Event(models.Model):
    """Event model."""
    name = models.CharField('Event name', max_length=255)
    description = models.TextField('Description')
    localization_name = models.CharField('Localization name', max_length=255)
    longitude = models.FloatField('Longitude', default=0.0)
    latitude = models.FloatField('Latitude', default=0.0)
    artists = models.ManyToManyField(Artist, verbose_name='Artists')
    date = models.DateTimeField('Event date')

    def __str__(self):  # noqa: D105
        return f'Event {self.name} at {self.date}'

    class Meta:  # noqa: D106
        verbose_name = 'Event'
        verbose_name_plural = 'Events'