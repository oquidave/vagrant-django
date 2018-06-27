# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voice', '0004_vhist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vhist',
        ),
    ]
