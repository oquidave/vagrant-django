# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20180627_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='smshist',
            name='name',
            field=models.CharField(max_length=25, default=datetime.datetime(2018, 7, 6, 7, 19, 52, 922018, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smshist',
            name='status',
            field=models.CharField(max_length=25),
        ),
    ]
