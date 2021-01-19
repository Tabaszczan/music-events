# Generated by Django 3.1.5 on 2021-01-19 18:12

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event name')),
                ('description', models.TextField(verbose_name='Description')),
                ('localization_name', models.CharField(max_length=255, verbose_name='Localization name')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326)),
                ('artist', models.ManyToManyField(to='artists.Artist', verbose_name='Artist')),
            ],
        ),
    ]
