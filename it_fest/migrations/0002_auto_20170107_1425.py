# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it_fest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='game_name',
            field=models.CharField(max_length=15, null=True, choices=[('cod', 'Call of Duty 4'), ('fifa', 'Fifa 17'), ('nfs', 'NFS Most Wanted')]),
        ),
        migrations.AlterField(
            model_name='registration',
            name='transaction_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
