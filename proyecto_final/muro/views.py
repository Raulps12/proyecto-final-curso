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

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse

from proyecto_final.aficionado.models import Perfil
from proyecto_final.aficionado.forms import UserForm, PerfilForm
from .models import Publicacion
from .forms import PublicacionForm, PerfilBusquedaAvanzadaForm
from django.db.models import Q

# Create your views here.


@login_required
# def muro(request, perfil_pk):
def muro(request):

    publicaciones_filtro = Publicacion.objects.filter(
        autor=request.user).order_by('-fecha_hora')

    # paginator = Paginator(publicaciones_filtro, settings.PAGINATION_PAGES)
    # page_default = 1

    # perfil = get_object_or_404(Perfil, pk=perfil_pk)

    # Aquí comprobamos si el usuario ya ha completado el formulario de registro
    if request.user.first_name == '':
        return redirect(reverse('registro_perfil'))
    # Final de comprobación

    else:
        """
        page = request.GET.get('page', page_default)
        try:
            publicaciones = paginator.page(page)
        except PageNotAnInteger:
            publicaciones = paginator.page(page_default)
        except EmptyPage:
            publicaciones = paginator.page(paginator.num_pages)
        """
        # context2 = {'publicaciones': publicaciones, 'perfil': perfil}
        # context2 = {'publicaciones': publicaciones, }
        context2 = {'publicaciones': publicaciones_filtro, }
        return render(request, 'muro.html', context2)


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
def editar_publicacion(request, publicacion_pk):
    publicacion_item = get_object_or_404(Publicacion, pk=publicacion_pk)
    publicacion_form = PublicacionForm(instance=publicacion_item)
    if request.method == 'POST':
        data = request.POST
        publicacion_form = PublicacionForm(data=data, instance=publicacion_item)
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

    return redirect(muro)


@login_required
def visita_muro(request, usuario_pk):

    usuario = User.objects.get(pk=usuario_pk)

    context = {'usuario': usuario, }
    return render(request, 'visita_muro.html', context)


"""
@login_required
@muro_decorator
def visita_muro(request, usuario_pk):

    context = {}
    return TemplateResponse(request, 'visita_muro.html', context)
"""


@login_required
def busqueda(request):

    usuarios = User.objects.filter(Q(username__icontains=request.GET['s']) | Q(
        first_name__icontains=request.GET['s']) | Q(last_name__icontains=request.GET['s']))

    context = {'usuarios': usuarios}
    return render(request, 'resultado_busqueda.html', context)


@login_required
def busqueda_avanzada(request):
    perfil_form = PerfilBusquedaAvanzadaForm()

    usuarios = Perfil.objects.filter(Q(pais__exact=request.GET['pais']) and Q(ciudad__exact=request.GET['ciudad']))

    # context = {'usuarios': usuarios}
    # return render(request, 'resultado_busqueda.html', context)
    context = {'perfil_form': perfil_form, 'usuarios': usuarios}
    return render(request, 'busqueda_avanzada.html', context)
