# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-01 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('1', 'Homme'), ('2', 'Femme')], max_length=1)),
                ('address', models.CharField(max_length=255)),
                ('postcode', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=255)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('information', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
