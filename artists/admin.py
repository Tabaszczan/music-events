from django.contrib import admin

# Register your models here.
from .models import Artist


@admin.register(Artist)
class EventAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'genre',
    ]