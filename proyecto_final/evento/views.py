# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import EventoForm, EventoEditarForm, EventoBusquedaAvanzadaForm
from .models import Evento
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from datetime import datetime, date, timedelta

# Create your views here.


@login_required
def crear_evento(request):
    evento_form = EventoForm()
    if request.method == 'POST':
        evento_form = EventoForm(request.POST, request.FILES)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            evento.autor = request.user
            evento_form.save()
            return redirect('muro')

    context = {'evento_form': evento_form, }
    return render(request, 'crear_evento.html', context)


@login_required
def editar_evento(request, evento_pk):
    evento_item = get_object_or_404(Evento, pk=evento_pk)
    evento_form = EventoEditarForm(instance=evento_item)
    if request.method == 'POST':
        evento_form = EventoEditarForm(request.POST, request.FILES, instance=evento_item)
        if evento_form.is_valid():
            evento = evento_form.save(commit=False)
            evento.autor = request.user
            evento.fecha_hora_creacion = datetime.now()
            evento_form.save()
            return redirect('muro')

    context = {'evento_form': evento_form, }
    return render(request, 'editar_evento.html', context)


@login_required
def eliminar_evento(request, evento_pk):

    evento = get_object_or_404(Evento, pk=evento_pk)

    evento.delete()

    return redirect(reverse('muro'))


@login_required
def ver_evento(request, evento_pk):
    evento = Evento.objects.get(pk=evento_pk)

    context = {'evento': evento, }

    return render(request, 'ver_evento.html', context)


@login_required
def busqueda_avanzada_eventos(request):
    busqueda_form = EventoBusquedaAvanzadaForm()
    context = {}

    if request.method == 'GET':
        # import ipdb; ipdb.set_trace()
        data = request.GET
        busqueda_form = EventoBusquedaAvanzadaForm(data=data)
        if busqueda_form.is_valid():
            eventos = Evento.objects.filter(pais=busqueda_form.cleaned_data[
                'pais'], ciudad=busqueda_form.cleaned_data['ciudad'],
                deportes__in=busqueda_form.cleaned_data['deportes']).distinct()
            context.update({'eventos': eventos})
            return render(request, 'resultado_busqueda_eventos.html', context)

    context.update({'busqueda_form': busqueda_form})
    return render(request, 'busqueda_eventos_avanzada.html', context)


@login_required
def evento_apuntarse(request, evento_pk):
    evento = Evento.objects.get(pk=evento_pk)

    evento.participantes.add(request.user)

    evento.save()

    return redirect(reverse('ver_evento', kwargs={'evento_pk': evento_pk}))


@login_required
def evento_desapuntarse(request, evento_pk):
    evento = Evento.objects.get(pk=evento_pk)

    evento.participantes.remove(request.user)

    evento.save()

    return redirect(reverse('ver_evento', kwargs={'evento_pk': evento_pk}))
