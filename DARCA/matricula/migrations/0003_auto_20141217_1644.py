# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_auto_20141217_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='secretaria',
            field=models.ForeignKey(null=True, to='matricula.Secretaria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='aluno',
            field=models.ManyToManyField(null=True, to='matricula.Aluno'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='secretaria',
            field=models.ForeignKey(null=True, to='matricula.Secretaria'),
            preserve_default=True,
        ),
    ]
