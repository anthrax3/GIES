# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-14 14:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=60)),
                ('user', models.CharField(max_length=60)),
                ('ip', models.CharField(max_length=20)),
                ('is_operated', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2016, 5, 14, 17, 58, 19, 622065))),
                ('last_updated', models.DateTimeField(default=datetime.datetime(2016, 5, 14, 17, 58, 19, 622093))),
                ('status', models.CharField(default='Bekliyor', max_length=15)),
                ('operated_by', models.CharField(default='-', max_length=60)),
            ],
        ),
    ]