# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_tipos'),
    ]

    operations = [
        migrations.AddField(
            model_name='lenguajes',
            name='tipo',
            field=models.CharField(default=11, max_length=40),
            preserve_default=False,
        ),
    ]
