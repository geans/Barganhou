# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20150923_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localinfo',
            name='latitude',
            field=models.DecimalField(decimal_places=8, max_digits=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='localinfo',
            name='longitude',
            field=models.DecimalField(decimal_places=8, max_digits=10, null=True, blank=True),
        ),
    ]
