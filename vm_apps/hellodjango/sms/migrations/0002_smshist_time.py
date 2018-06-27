# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smshist',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 26, 12, 49, 30, 600547, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
