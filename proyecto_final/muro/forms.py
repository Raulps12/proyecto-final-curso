# -*- encoding: utf-8 -*-
from django import forms
from .models import Publicacion


class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion
        fields = ['titulo', 'video', 'imagen', 'texto']
