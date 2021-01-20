from django.contrib import admin

# Register your models here.
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin view for Event."""

    list_display = [
        'name',
        'description',
        'localization_name',
        'coordinates',
    ]