# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-28 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', max_length=50, null=True, verbose_name='Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
