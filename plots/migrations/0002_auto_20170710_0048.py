# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walmartmodel',
            name='brandName',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='walmartmodel',
            name='largeImage',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='walmartmodel',
            name='name',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='walmartmodel',
            name='stock',
            field=models.CharField(max_length=60),
        ),
    ]
