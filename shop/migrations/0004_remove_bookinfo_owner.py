# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 08:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20161221_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='owner',
        ),
    ]
