# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0003_remove_fwno_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vhist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=13)),
                ('dest', models.CharField(max_length=13)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
