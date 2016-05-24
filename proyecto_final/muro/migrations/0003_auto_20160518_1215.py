# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0002_auto_20160518_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]