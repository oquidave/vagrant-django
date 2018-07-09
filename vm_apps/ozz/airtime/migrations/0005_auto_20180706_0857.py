# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airtime', '0004_auto_20180706_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bulkhist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='buyhist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
