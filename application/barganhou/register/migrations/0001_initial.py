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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('amount', models.IntegerField(default=1)),
                ('date_log', models.DateTimeField()),
                ('local', models.CharField(max_length=30)),
                ('pucharse', models.CharField(max_length=3)),
            ],
        ),
    ]
