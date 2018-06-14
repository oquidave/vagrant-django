# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airtime', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyhist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
            ],
        ),
    ]
