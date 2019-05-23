# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-22 12:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0007_auto_20190522_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField(auto_now_add=True, null=True)),
                ('voted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.Image')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='imagevote',
            unique_together=set([('voter', 'voted')]),
        ),
    ]