# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='pucharse',
            field=models.CharField(max_length=3, choices=[('Y', 'yes'), ('N', 'no')]),
        ),
    ]
