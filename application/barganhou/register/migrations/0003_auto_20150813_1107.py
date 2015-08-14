# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150813_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='date_log',
            field=models.DateField(),
        ),
    ]
