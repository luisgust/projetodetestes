# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('aluno', models.ManyToManyField(to='matricula.Aluno')),
                ('secretaria', models.ForeignKey(to='matricula.Secretaria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='disciplinas',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='disciplinas',
            name='secretaria',
        ),
        migrations.DeleteModel(
            name='Disciplinas',
        ),
    ]
