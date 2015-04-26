# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0003_auto_20150426_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='create',
            options={'ordering': ['art'], 'managed': False},
        ),
    ]
