# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_gameroom_accepting_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='unlocked',
            field=models.BooleanField(default=False),
        ),
    ]