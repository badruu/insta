# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-17 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='leopard.jpg', upload_to='images')),
                ('img_name', models.CharField(default='My Photo', max_length=30)),
                ('img_caption', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
