# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-08 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('specialty', models.CharField(default='', max_length=100)),
                ('organization', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
