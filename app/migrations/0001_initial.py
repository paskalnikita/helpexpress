# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=512)),
                ('phone', models.CharField(max_length=512)),
                ('message', models.CharField(max_length=512)),
            ],
        ),
    ]
