# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_remove_perfil_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='dtNascimento',
            field=models.CharField(max_length=10, verbose_name=b'Data de Nascimento'),
            preserve_default=True,
        ),
    ]
