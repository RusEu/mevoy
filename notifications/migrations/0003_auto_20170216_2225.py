# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 22:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_notification_department'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-datetime']},
        ),
    ]
