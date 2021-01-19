"""Models artists."""
from django.db import models


# Create your models here.


class Artist(models.Model):
    """Artist model."""
    name = models.CharField('Artist name', max_length=255)
    genre = models.CharField('Music genre', max_length=255)
