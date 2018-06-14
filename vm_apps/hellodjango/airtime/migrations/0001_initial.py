# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
            ],
        ),
    ]
