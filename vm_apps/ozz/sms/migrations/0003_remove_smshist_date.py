# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_smshist_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smshist',
            name='date',
        ),
    ]
