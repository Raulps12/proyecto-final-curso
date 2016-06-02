# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import Perfil
from datetimewidget.widgets import DateWidget  # , TimeWidget, DateTimeWidget
# from allauth.account.forms import UserForm
# as AllAuthUserForm, SetPasswordField, PasswordField

from dal import autocomplete


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Nombre', 'autofocus': 'autofocus', 'required': 'true'}),
            'last_name': forms.TextInput(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Apellidos', 'required': 'true'}),
        }


class PerfilForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True,
            'startView': 4,
            'showMeridian': True
        }
        model = Perfil
        fields = ['pais', 'ciudad', 'descripcion',
                  'fecha_nac', 'profesional', 'deportes']
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'fecha_nac': DateWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions, attrs={'class': 'datetimepicker', 'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Descripción', 'required': 'true', 'id': 'descripcion'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true', 'id': 'ciudad'})
        }


class PerfilAdminForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('__all__')
        widgets = {
            'deportes': forms.widgets.CheckboxSelectMultiple(attrs={'title': 'deporte'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Descripción'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'])
        }


class PerfilEditarForm(forms.ModelForm):

    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True,
            'startView': 4,
            'showMeridian': True
        }
        model = Perfil
        fields = ['pais', 'ciudad', 'descripcion',
                  'fecha_nac', 'profesional']
        widgets = {
            'fecha_nac': DateWidget(usel10n=True, bootstrap_version=3, options=dateTimeOptions, attrs={'class': 'datetimepicker', 'required': 'true'}),
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Descripción', 'required': 'true', 'id': 'descripcion'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete', attrs={'required': 'true'}),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'], attrs={'required': 'true'})
        }


class PerfilEditarAdminForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ('__all__')
        widgets = {
            'descripcion': forms.Textarea(
                attrs={'class': 'textinput form-control input-lg', 'placeholder': 'Descripción'}),
            'pais': autocomplete.ModelSelect2(url='country-autocomplete'),
            'ciudad': autocomplete.ModelSelect2(url='city-autocomplete', forward=['pais'])
        }
