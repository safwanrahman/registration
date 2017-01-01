# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it_fest', '0002_auto_20170101_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='game_name',
            field=models.CharField(max_length=15, choices=[('Call Of Duty 4', 'Call Of Duty 4'), ('Fifa 17', 'Fifa 17'), ('NFS Most Wanted', 'NFS Most Wanted')]),
        ),
    ]
