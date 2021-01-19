"""Models artists."""
from django.db import models


# Create your models here.


class Artist(models.Model):
    """Artist model."""
    name = models.CharField('Artist name', max_length=255)
    genre = models.CharField('Music genre', max_length=255)

    def __str__(self):  # noqa: D105
        return f'Artist: {self.name}, Genre: {self.genre}'

    class Meta:  # noqa: D106
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'