# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-06 11:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('find_ur_home', '0005_auto_20171105_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='for_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
