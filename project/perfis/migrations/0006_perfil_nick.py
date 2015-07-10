# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_auto_20150710_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nick',
            field=models.SlugField(default='', verbose_name=b'Nick'),
            preserve_default=False,
        ),
    ]
