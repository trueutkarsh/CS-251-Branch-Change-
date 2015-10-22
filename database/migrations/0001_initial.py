# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('rollno', models.CharField(max_length=9)),
                ('cpi', models.FloatField()),
                ('category', models.CharField(max_length=2)),
                ('branchops', models.ManyToManyField(related_name='usr', to='database.program')),
                ('currentbranch', models.ForeignKey(related_name='user', to='database.program')),
            ],
        ),
    ]
