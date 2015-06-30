# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20150629_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imperativo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=40)),
                ('autores', models.CharField(max_length=40)),
                ('editor', models.CharField(max_length=40)),
            ],
        ),
        migrations.RenameModel(
            old_name='Libro',
            new_name='Declarativo',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
    ]
