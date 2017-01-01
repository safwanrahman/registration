# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it_fest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='registration',
            field=models.ForeignKey(to='it_fest.Registration', null=True),
        ),
    ]
