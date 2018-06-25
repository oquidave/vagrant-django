# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0002_auto_20180622_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fwno',
            name='add_date',
        ),
    ]
