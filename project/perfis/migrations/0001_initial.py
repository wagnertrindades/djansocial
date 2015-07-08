# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('slug', models.SlugField(verbose_name=b'Atalho')),
                ('email', models.CharField(max_length=100, verbose_name=b'E-mail')),
                ('dtNascimento', models.DateField(verbose_name=b'Data de Nascimento')),
                ('localidade', models.CharField(max_length=255, verbose_name=b'Localidade', blank=True)),
                ('cargo', models.CharField(max_length=155, null=True, verbose_name=b'Cargo')),
                ('empresa', models.CharField(max_length=155, null=True, verbose_name=b'Empresa')),
                ('curso', models.CharField(max_length=155, null=True, verbose_name=b'Curso')),
                ('escola', models.CharField(max_length=155, null=True, verbose_name=b'Escola')),
                ('dtCadastro', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('dtAtualizacao', models.DateTimeField(auto_now=True, verbose_name=b'Atualizado em')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ForeignKey(related_name='convites_recebidos', to='perfis.Perfil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='convite',
            name='solicitante',
            field=models.ForeignKey(related_name='convites_feitos', to='perfis.Perfil'),
            preserve_default=True,
        ),
    ]
