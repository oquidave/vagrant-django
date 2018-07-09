# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('airtime', '0003_bulkhist'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkhist',
            name='name',
            field=models.CharField(max_length=25, default=datetime.datetime(2018, 7, 6, 7, 19, 21, 114521, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='athist',
            name='amount',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='athist',
            name='destination',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='athist',
            name='source',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='athist',
            name='status',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='bulkhist',
            name='amount',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='bulkhist',
            name='destination',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='bulkhist',
            name='status',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='buyhist',
            name='amount',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='buyhist',
            name='destination',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='buyhist',
            name='status',
            field=models.CharField(max_length=25),
        ),
    ]
