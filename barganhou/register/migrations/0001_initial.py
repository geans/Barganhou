# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.DecimalField(max_digits=11, decimal_places=2)),
                ('amount', models.IntegerField()),
                ('date_log', models.DateField()),
                ('local', models.CharField(max_length=30)),
                ('pucharse', models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=3)),
            ],
        ),
    ]
