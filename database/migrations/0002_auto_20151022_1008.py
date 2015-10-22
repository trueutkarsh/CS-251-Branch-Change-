# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='currstrength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='program',
            name='sancstrength',
            field=models.IntegerField(default=0),
        ),
    ]
