"""Models events."""
# Create your models here.
# Django
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from django.db import models

# Project
from artists.models import Artist


class Event(models.Model):
    """Event model."""
    name = models.CharField('Event name', max_length=255)
    description = models.TextField('Description')
    localization_name = models.CharField('Localization name', max_length=255)
    location = gismodels.PointField(geography=True, default=Point(0.0, 0.0))
    artists = models.ManyToManyField(Artist, verbose_name='Artists')
    date = models.DateTimeField('Event date')

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y

    def __str__(self):  # noqa: D105
        return f'Event {self.name}'

    class Meta:  # noqa: D106
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
