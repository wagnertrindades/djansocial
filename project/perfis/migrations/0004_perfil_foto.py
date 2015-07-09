# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_auto_20150708_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='foto',
            field=models.ImageField(upload_to=b'perfis/images', null=True, verbose_name=b'Foto', blank=True),
            preserve_default=True,
        ),
    ]
