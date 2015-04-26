# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'artist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('art_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('region', models.CharField(max_length=32)),
                ('style', models.CharField(max_length=32, null=True, blank=True)),
                ('type', models.CharField(max_length=32, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('piclink', models.TextField(null=True, db_column='picLink', blank=True)),
            ],
            options={
                'db_table': 'art_piece',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
            ],
            options={
                'db_table': 'create',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('type', models.CharField(max_length=45, null=True, blank=True)),
                ('belongto_event_id', models.IntegerField(null=True, db_column='belongTo_event_id', blank=True)),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('museum_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('parking', models.TextField(null=True, blank=True)),
                ('website', models.CharField(max_length=45)),
                ('location', models.TextField()),
                ('phone', models.CharField(max_length=32)),
                ('hours', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'museum',
                'managed': False,
            },
        ),
    ]
