# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-11 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170210_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='need',
            name='appointment',
        ),
        migrations.AddField(
            model_name='appointment',
            name='need',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='event.Need'),
            preserve_default=False,
        ),
    ]
