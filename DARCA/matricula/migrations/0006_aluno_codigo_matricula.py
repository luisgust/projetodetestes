# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0005_auto_20141217_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='codigo_matricula',
            field=models.CharField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
