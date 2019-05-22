# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-22 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20190522_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='down_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='up_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
