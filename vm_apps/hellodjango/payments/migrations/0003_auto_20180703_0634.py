# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_remove_payhist_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='payhist',
            name='status',
            field=models.CharField(max_length=25, default=datetime.datetime(2018, 7, 3, 6, 34, 29, 854036, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
