# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-20 17:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20160520_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackContactNo',
            new_name='contactNo',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackEmailAddr',
            new_name='emailAddr',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackType',
            new_name='fbtype',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackFullname',
            new_name='fullname',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackMessage',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='fbackTimeStamp',
            new_name='timeStamp',
        ),
    ]