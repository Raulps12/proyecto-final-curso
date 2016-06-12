# -*- encoding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# from .decorators import muro_decorator
from django.template.response import TemplateResponse
from datetime import datetime, date, timedelta

from django.core.urlresolvers import reverse

from proyecto_final.aficionado.models import Perfil
from proyecto_final.evento.models import Evento
from proyecto_final.aficionado.forms import UserForm, PerfilForm
from .models import Publicacion, Comentario
from .forms import PublicacionForm, PerfilBusquedaAvanzadaForm, ComentarioForm
from django.db.models import Q

# Create your views here.


@login_required
def muro(request, template='muro.html', page_template='muro_page.html'):

    publicaciones_filtro = Publicacion.objects.filter(
        autor=request.user).order_by('-fecha_hora')

    eventos_filtro = Evento.objects.filter(
        autor=request.user).order_by('fecha_hora')

    # Aquí comprobamos si el usuario ya ha completado el formulario de registro
    if request.user.first_name == '':
        return redirect(reverse('registro_perfil'))
    # Final de comprobación

    else:
        context = {'publicaciones': publicaciones_filtro, 'eventos': eventos_filtro,
                   'page_template': page_template, }
        if request.is_ajax():
            template = page_template
        return render(request, template, context)


@login_required
def visita_muro(request, usuario_pk, template='visita_muro.html', page_template='visita_muro_page.html'):
    usuario = User.objects.get(pk=usuario_pk)

    publicaciones_filtro = Publicacion.objects.filter(
        autor=usuario.id).order_by('-fecha_hora')

    comentario_form = ComentarioForm()

    context = {'usuario': usuario, 'publicaciones': publicaciones_filtro,
               'comentario_form': comentario_form,
               'page_template': page_template, }
    if request.is_ajax():
        template = page_template
    return render(request, template, context)


"""
@login_required
@muro_decorator
def visita_muro(request, usuario_pk):

    context = {}
    return TemplateResponse(request, 'visita_muro.html', context)
"""


@login_required
def crear_publicacion(request):
    publicacion_form = PublicacionForm()
    if request.method == 'POST':
        publicacion_form = PublicacionForm(request.POST, request.FILES)
        if publicacion_form.is_valid():
            publicacion = publicacion_form.save(commit=False)
            publicacion.autor = request.user
            publicacion_form.save()
            return redirect('muro')

    context = {'publicacion_form': publicacion_form, }
    return render(request, 'crear_publicacion.html', context)


@login_required
def crear_comentario(request, publicacion_pk, usuario_pk):
    usuario = User.objects.get(pk=usuario_pk)

    publicaciones_filtro = Publicacion.objects.filter(
        autor=usuario.id).order_by('-fecha_hora')

    comentario_form = ComentarioForm()
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.autor = request.user
            # comentario.fecha_hora = datetime.now()
            comentario.publicacion_id = publicacion_pk
            comentario_form.save()
            return redirect(request.META.get('HTTP_REFERER'))

    context = {'usuario': usuario, 'publicaciones': publicaciones_filtro,
               'comentario_form': comentario_form, }
    return render(request, 'visita_muro.html', context)


@login_required
def editar_publicacion(request, publicacion_pk):
    publicacion_item = get_object_or_404(Publicacion, pk=publicacion_pk)
    publicacion_form = PublicacionForm(instance=publicacion_item)
    if request.method == 'POST':
        data = request.POST
        publicacion_form = PublicacionForm(
            data=data, instance=publicacion_item)
        if publicacion_form.is_valid():
            publicacion = publicacion_form.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_hora = datetime.now()
            publicacion_form.save()
            return redirect('muro')

    context = {'publicacion_form': publicacion_form, }
    return render(request, 'editar_publicacion.html', context)


@login_required
def eliminar_publicacion(request, publicacion_pk):

    publicacion = get_object_or_404(Publicacion, pk=publicacion_pk)

    publicacion.delete()

    return redirect(reverse('muro'))


@login_required
def busqueda(request):

    usuarios = User.objects.filter(Q(username__icontains=request.GET['s']) | Q(
        first_name__icontains=request.GET['s']) | Q(last_name__icontains=request.GET['s']))

    context = {'usuarios': usuarios}
    return render(request, 'resultado_busqueda.html', context)


@login_required
def busqueda_avanzada(request):
    busqueda_form = PerfilBusquedaAvanzadaForm()
    context = {}

    if request.method == 'GET':
        # import ipdb; ipdb.set_trace()
        data = request.GET
        busqueda_form = PerfilBusquedaAvanzadaForm(data=data)
        if busqueda_form.is_valid():
            # usuarios = Perfil.objects.filter(pais=request.GET['pais'], ciudad=request.GET['ciudad'])
            perfiles = Perfil.objects.filter(pais=busqueda_form.cleaned_data[
                                             'pais'], ciudad=busqueda_form.cleaned_data['ciudad'],
                                             deportes__in=busqueda_form.cleaned_data['deportes']).distinct()
            context.update({'perfiles': perfiles})
            return render(request, 'resultado_busqueda.html', context)

    context.update({'busqueda_form': busqueda_form})
    return render(request, 'busqueda_avanzada.html', context)
