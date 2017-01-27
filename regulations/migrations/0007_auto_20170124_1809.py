# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulations', '0006_auto_20170124_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulation',
            name='DC_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_identifier',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_language',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_publisher',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_source',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_subject',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regulation',
            name='DC_type',
            field=models.TextField(blank=True),
        ),
    ]
