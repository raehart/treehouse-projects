# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_truefalsequestion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MultipleChoiceQuestions',
            new_name='MultipleChoiceQuestion',
        ),
    ]