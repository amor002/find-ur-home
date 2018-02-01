# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-05 16:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('find_ur_home', '0003_auto_20171104_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('image', models.FileField(default='user_img.png', upload_to='users_images/')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_information',
            name='user',
        ),
        migrations.DeleteModel(
            name='user_information',
        ),
    ]