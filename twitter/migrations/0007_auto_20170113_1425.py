# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_auto_20170113_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='mug_shot',
            field=models.ImageField(blank=True, null=True, upload_to='/uploads/mugs'),
        ),
    ]
