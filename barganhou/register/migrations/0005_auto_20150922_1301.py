# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20150922_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localinfo',
            name='state',
            field=models.CharField(max_length=19, default='AL', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('AP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='date_log',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='pucharse',
            field=models.CharField(max_length=3, default='Y', choices=[('Y', 'yes'), ('N', 'no')]),
        ),
    ]
