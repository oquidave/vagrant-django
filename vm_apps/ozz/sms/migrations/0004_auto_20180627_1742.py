# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_remove_smshist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smshist',
            name='time',
        ),
        migrations.AddField(
            model_name='smshist',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 6, 27, 17, 42, 14, 878621, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
