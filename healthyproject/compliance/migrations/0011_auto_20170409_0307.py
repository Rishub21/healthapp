# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-09 03:07
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compliance', '0010_auto_20170408_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='initial',
            old_name='conditions',
            new_name='feedback',
        ),
        migrations.AddField(
            model_name='patient',
            name='feedback',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
