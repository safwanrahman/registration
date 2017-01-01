# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=14)),
                ('institute', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_name', models.CharField(max_length=15, null=True, choices=[('cod', 'Call of Duty 4'), ('fifa', 'Fifa 17'), ('nfsmw', 'NFS Most Wanted')])),
                ('payment_status', models.CharField(default='pending', max_length=15, choices=[('pending', 'Pending'), ('verified', 'Verified')])),
                ('transaction_id', models.BigIntegerField()),
                ('bkash_mobile_number', models.CharField(max_length=14)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='registration',
            field=models.ForeignKey(to='it_fest.Registration', null=True),
        ),
    ]
