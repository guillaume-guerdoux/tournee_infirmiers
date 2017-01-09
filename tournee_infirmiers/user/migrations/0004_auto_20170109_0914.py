# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-09 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170108_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='namesurname@domain.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='Pierre', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Durand', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default='0102030405', max_length=255),
            preserve_default=False,
        ),
    ]