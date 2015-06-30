# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='editor',
            old_name='model',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publicacion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='portada',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autores',
        ),
        migrations.AddField(
            model_name='libro',
            name='autores',
            field=models.CharField(default=122, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='editor',
            field=models.CharField(max_length=40),
        ),
    ]
