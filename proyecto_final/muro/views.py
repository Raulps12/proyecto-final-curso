# -*- encoding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from proyecto_final.aficionado.models import Perfil
from proyecto_final.aficionado.forms import UserForm, PerfilForm
from .models import Publicacion
from .forms import PublicacionForm

# Create your views here.


@login_required
# def muro(request, perfil_pk):
def muro(request):

    publicaciones_filtro = Publicacion.objects.filter(
        autor=request.user).order_by('-fecha_hora')

    paginator = Paginator(publicaciones_filtro, settings.PAGINATION_PAGES)
    page_default = 1

    # perfil = get_object_or_404(Perfil, pk=perfil_pk)

    # Aquí comprobamos si el usuario ya ha completado el formulario de registro
    user_form = UserForm(instance=request.user)
    perfil_form = PerfilForm(instance=Perfil.objects.get(owner=request.user))
    if request.method == 'POSfT':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(
            request.POST, instance=Perfil.objects.get(owner=request.user))
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()

    if request.user.first_name == '':
        context = {'user_form': user_form, 'perfil_form': perfil_form, }
        return render(request, 'registro_perfil.html', context)
    # Final de comprobación

    else:

        page = request.GET.get('page', page_default)
        try:
            publicaciones = paginator.page(page)
        except PageNotAnInteger:
            publicaciones = paginator.page(page_default)
        except EmptyPage:
            publicaciones = paginator.page(paginator.num_pages)
        # context2 = {'publicaciones': publicaciones, 'perfil': perfil}
        context2 = {'publicaciones': publicaciones, }
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
