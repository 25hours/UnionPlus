# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-31 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0003_auto_20170531_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]
