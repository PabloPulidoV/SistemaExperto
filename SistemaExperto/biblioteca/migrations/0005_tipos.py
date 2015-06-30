# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20150629_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('tipo1', models.CharField(max_length=40)),
            ],
        ),
    ]
