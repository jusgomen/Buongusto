# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='category',
            field=models.CharField(choices=[('BR', 'Breakfast'), ('CH', 'Lunch'), ('DN', 'Dinner')], default='CH', max_length=2),
            preserve_default=False,
        ),
    ]
