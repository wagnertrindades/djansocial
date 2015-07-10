# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_perfil_foto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['nome'], 'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cargo',
            field=models.CharField(max_length=155, null=True, verbose_name=b'Cargo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='curso',
            field=models.CharField(max_length=155, null=True, verbose_name=b'Curso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='empresa',
            field=models.CharField(max_length=155, null=True, verbose_name=b'Empresa', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='escola',
            field=models.CharField(max_length=155, null=True, verbose_name=b'Escola', blank=True),
            preserve_default=True,
        ),
    ]
