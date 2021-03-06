# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulations', '0003_auto_20170124_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='regulation',
            name='subject',
        ),
        migrations.AddField(
            model_name='regulation',
            name='subjects',
            field=models.ManyToManyField(to='regulations.Subjects'),
        ),
    ]
