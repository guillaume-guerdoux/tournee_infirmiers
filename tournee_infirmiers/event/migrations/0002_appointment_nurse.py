# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-01 08:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Nurse'),
        ),
    ]
