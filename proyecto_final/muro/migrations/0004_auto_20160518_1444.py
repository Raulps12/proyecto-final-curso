# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 12:44
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0003_auto_20160518_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Video'),
        ),
    ]