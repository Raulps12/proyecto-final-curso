# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('fecha_hora', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y Hora')),
                ('video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Video')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_publicacion', verbose_name='Imagen')),
                ('texto', models.TextField(blank=True, max_length=240, null=True, verbose_name='Text')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to=settings.AUTH_USER_MODEL, verbose_name='Propietario')),
            ],
            options={
                'verbose_name': 'publicacion',
                'verbose_name_plural': 'publicaciones',
            },
        ),
    ]
