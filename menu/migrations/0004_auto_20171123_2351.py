# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-23 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_order_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tables',
            name='price',
        ),
        migrations.AddField(
            model_name='customers',
            name='table',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Tables'),
        ),
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[('payed', 'Payed'), ('ready', 'Ready'), ('pending', 'Pending')], default='pending', max_length=7),
        ),
    ]
