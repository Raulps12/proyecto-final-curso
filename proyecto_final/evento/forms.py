# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Evento
from datetimewidget.widgets import DateWidget, TimeWidget, DateTimeWidget


class EventoForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ['titulo', 'imagen', 'fecha_hora', 'descripcion', 'deportes',
                  'precio', 'max_participantes', 'direccion', 'localizacion']
        widgets = {
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions),
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
        }


class EventoAdminForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ('__all__')
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
        }
