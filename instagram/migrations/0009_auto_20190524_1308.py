# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-24 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20190522_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='date_posted',
            new_name='timestamp',
        ),
    ]