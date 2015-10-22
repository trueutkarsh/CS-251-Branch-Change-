# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20151022_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(max_length=2, choices=[(b'GE', b'GENERAL'), (b'SC', b'SCHEDULE CASTE'), (b'ST', b'SCHEDULE TRIBES'), (b'OB', b'OTHER BACKWARD CLASSES')]),
        ),
    ]
