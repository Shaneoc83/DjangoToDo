# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='stripe_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscription_end',
        ),
    ]
