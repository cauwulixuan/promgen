# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 03:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0025_shard_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['shard', 'name']},
        ),
    ]