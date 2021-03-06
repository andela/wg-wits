# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-15 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20160303_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='APIKeyUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='add_user',
            field=models.BooleanField(default=False, help_text='Check eligibility of this user to create users via the REST API', verbose_name='Field to verify whether a particular user can add other users via the REST API'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rest_api_user',
            field=models.BooleanField(default=False, help_text='Boolean value to show whether this user was created via the REST API or it is a wger user instance', verbose_name='Who created this user'),
        ),
        migrations.AlterField(
            model_name='license',
            name='full_name',
            field=models.CharField(help_text='If a license has been localized, e.g. the Creative Commons licenses for the different countries, add them as separate entries here.', max_length=60, verbose_name='Full name'),
        ),
    ]
