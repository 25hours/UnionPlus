# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-31 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuthentication', '0006_auto_20170531_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='管理员'),
        ),
    ]