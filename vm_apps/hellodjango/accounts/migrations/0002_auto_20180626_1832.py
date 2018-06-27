# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='User_name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='accounts',
            name='user_name',
            field=models.CharField(max_length=20, default=datetime.datetime(2018, 6, 26, 18, 32, 20, 119575, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
