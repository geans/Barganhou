# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150817_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=19, default='Alagoas', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('AP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('city', models.CharField(default='Maceió', max_length=50)),
                ('cep', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(max_length=300)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('neighborhood', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='local',
            field=models.ForeignKey(to='register.LocalInfo'),
        ),
    ]
