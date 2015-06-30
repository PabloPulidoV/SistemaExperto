# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_auto_20150629_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lenguajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Declarativo',
        ),
        migrations.RenameField(
            model_name='imperativo',
            old_name='autores',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='imperativo',
            name='editor',
        ),
        migrations.RemoveField(
            model_name='imperativo',
            name='titulo',
        ),
    ]
