# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='index',
            field=models.IntegerField(),
        ),
    ]