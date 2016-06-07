# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0006_auto_20160530_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Autor', related_name='author_comments'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.ForeignKey(to='muro.Publicacion', verbose_name='Publicación', related_name='comments'),
        ),
    ]
