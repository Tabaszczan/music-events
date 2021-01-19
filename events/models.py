"""Models events."""
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.
from artists.models import Artist


class Event(models.Model):
    """Event model."""
    name = models.CharField('Event name', max_length=255)
    description = models.TextField('Description')
    localization_name = models.CharField('Localization name', max_length=255)
    coordinates = models.PointField('Coordinates', geography=True, default=Point(0.0, 0.0))
    artists = models.ManyToManyField(Artist, verbose_name='Artists')
    date = models.DateTimeField('Event date')

    @property
    def longitude(self):
        return self.coordinates.x

    @property
    def latitude(self):
        return self.coordinates.y

    def __str__(self):  # noqa: D105
        return f'Event {self.name} at {self.date}'

    class Meta:  # noqa: D106
        verbose_name = 'Event'
        verbose_name_plural = 'Events'