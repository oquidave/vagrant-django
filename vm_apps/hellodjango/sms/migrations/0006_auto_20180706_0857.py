# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20180706_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smshist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
