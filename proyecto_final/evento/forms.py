# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Evento
from datetimewidget.widgets import DateWidget, TimeWidget, DateTimeWidget
from dal import autocomplete


class EventoForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ['titulo', 'imagen', 'fecha_hora', 'descripcion', 'deportes', 'pais', 'ciudad',
                  'precio', 'max_participantes', 'direccion', 'localizacion']
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'textinput form-control input-md', 'autofocus': 'autofocus', 'required': 'true'}),
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions, attrs={'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'required': 'true', 'id': 'descripcion'}),
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control input-md', 'id': 'imagen_evento', 'required': 'true'}),
            'precio': forms.TextInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'max_participantes': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'precio': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'direccion': forms.TextInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
        }


class EventoAdminForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ('__all__')
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'textinput form-control input-md', 'autofocus': 'autofocus', 'required': 'true'}),
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions, attrs={'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'required': 'true', 'id': 'descripcion'}),
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control input-md', 'id': 'imagen_evento', 'required': 'true'}),
            'precio': forms.TextInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'max_participantes': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'precio': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'direccion': forms.TextInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
        }


class EventoEditarForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy hh:ii',
            'autoclose': True,
            'startView': 2,
            'showMeridian': True
        }
        model = Evento
        fields = ['titulo', 'imagen', 'descripcion', 'fecha_hora', 'pais', 'ciudad',
                  'precio', 'max_participantes']
        widgets = {
            'titulo': forms.TextInput(
                attrs={'class': 'textinput form-control input-md', 'autofocus': 'autofocus', 'required': 'true'}),
            'fecha_hora': DateTimeWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions, attrs={'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'required': 'true', 'id': 'descripcion'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control input-md', 'id': 'imagen_evento', 'required': 'true'}),
            'precio': forms.TextInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'max_participantes': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
            'precio': forms.NumberInput(attrs={'class': 'textinput form-control input-md', 'required': 'true'}),
        }


class EventoBusquedaAvanzadaForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ['pais', 'ciudad', 'deportes']
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true'})
        }
