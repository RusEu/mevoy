# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='approvals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requesttype',
            name='approvals',
            field=models.IntegerField(default=1),
        ),
    ]
