# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('images', models.FileField(upload_to=b'')),
                ('desc', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
