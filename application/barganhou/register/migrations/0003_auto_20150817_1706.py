# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150817_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
