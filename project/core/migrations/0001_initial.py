# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('dtNascimento', models.CharField(max_length=10)),
                ('localidade', models.CharField(max_length=255, null=True)),
                ('cargo', models.CharField(max_length=155, null=True)),
                ('empresa', models.CharField(max_length=155, null=True)),
                ('curso', models.CharField(max_length=155, null=True)),
                ('escola', models.CharField(max_length=155, null=True)),
                ('dtCadastro', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
