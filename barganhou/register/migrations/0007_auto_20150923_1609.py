# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20150922_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='localinfo',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='localinfo',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True),
        ),
    ]
