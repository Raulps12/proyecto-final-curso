# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import EventoForm
from django.contrib.auth.decorators import login_required

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
