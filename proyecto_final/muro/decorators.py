# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def muro_decorator(view):

    def wrapper(request, usuario_pk):

        usuario = get_object_or_404(User, pk=usuario_pk)

        r = view(request, usuario_pk)

        r.context_data.update({'usuario': usuario})

        return r.render()

    return wrapper
