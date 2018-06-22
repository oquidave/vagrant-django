# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fwno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('number', models.CharField(max_length=13)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
