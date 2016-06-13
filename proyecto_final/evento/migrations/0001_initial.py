# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import location_field.models.plain
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aficionado', '0004_auto_20160513_0833'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('titulo', models.CharField(verbose_name='Título', max_length=200)),
                ('imagen', models.ImageField(verbose_name='Imagen', upload_to='imagenes_evento')),
                ('fecha_hora_creacion', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y Hora creación')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y Hora')),
                ('descripcion', models.TextField(verbose_name='Descripción', max_length=250)),
                ('precio', models.IntegerField(null=True, verbose_name='Precio', blank=True)),
                ('max_participantes', models.IntegerField(null=True, verbose_name='Máximo participantes', blank=True)),
                ('direccion', models.CharField(verbose_name='Dirección', max_length=255)),
                ('localizacion', location_field.models.plain.PlainLocationField(verbose_name='Localización', max_length=63)),
                ('autor', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL, related_name='author_event')),
                ('ciudad', models.ForeignKey(null=True, verbose_name='Ciudad', to='aficionado.City', blank=True)),
                ('deportes', models.ManyToManyField(verbose_name='Deportes', to='aficionado.Deporte', related_name='deportes')),
                ('pais', models.ForeignKey(null=True, verbose_name='País', to='aficionado.Country', blank=True)),
                ('participantes', models.ManyToManyField(verbose_name='Participantes', to=settings.AUTH_USER_MODEL, related_name='participantes')),
            ],
            options={
                'verbose_name_plural': 'eventos',
                'verbose_name': 'evento',
            },
        ),
    ]
