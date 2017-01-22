# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-19 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('availability', '0002_availability_availability_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabilitygroup',
            name='nurse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Nurse'),
            preserve_default=False,
        ),
    ]