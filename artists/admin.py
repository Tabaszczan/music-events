"""Artists admin."""
# Django
from django.contrib import admin

# Local
from .models import Artist


@admin.register(Artist)
class EventAdmin(admin.ModelAdmin):
    """Event admin view registration."""

    list_display = [
        'name',
        'genre',
    ]
