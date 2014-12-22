# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0006_aluno_codigo_matricula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='creditos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='creditos',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplina',
            name='discipinas',
            field=models.ManyToManyField(null=True, to='matricula.Disciplina'),
            preserve_default=True,
        ),
    ]
