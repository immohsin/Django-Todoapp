# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 07:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2017, 9, 9, 7, 10, 36, 466832))),
            ],
        ),
    ]