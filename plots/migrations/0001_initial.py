# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 22:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WalmartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upc', models.CharField(max_length=50, unique=True)),
                ('salePrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('name', models.CharField(max_length=1000)),
                ('brandName', models.CharField(max_length=1000)),
                ('modelNumber', models.CharField(max_length=1000)),
                ('largeImage', models.CharField(max_length=1000)),
                ('stock', models.CharField(max_length=50)),
                ('freeShippingOver50Dollars', models.BooleanField()),
                ('date_modified', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
