# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-24 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusinfo',
            name='catalogueCodes',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='colorTombstone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='howManyTombstones',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='installationDate',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='locationPersonal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='locationTombstone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contactusinfo',
            name='otherInfo',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
