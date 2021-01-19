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
    coordinates = models.PointField(geography=True, default=Point(0.0, 0.0))
    artists = models.ManyToManyField(Artist, verbose_name='Artists')