# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20150922_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
