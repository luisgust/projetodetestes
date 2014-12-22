# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_auto_20141217_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='secretaria',
            field=models.ForeignKey(null=True, blank=True, to='matricula.Secretaria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='aluno',
            field=models.ManyToManyField(to='matricula.Aluno', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='secretaria',
            field=models.ForeignKey(null=True, blank=True, to='matricula.Secretaria'),
            preserve_default=True,
        ),
    ]
