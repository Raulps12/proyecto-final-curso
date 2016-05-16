# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from proyecto_final.aficionado.models import Perfil
from proyecto_final.aficionado.forms import UserForm, PerfilForm

# Create your views here.


@login_required
def muro(request):
	user_form = UserForm(instance=request.user)
	perfil_form = PerfilForm(instance=Perfil.objects.get(owner=request.user))
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		perfil_form = PerfilForm(request.POST, instance=Perfil.objects.get(owner=request.user))
		if user_form.is_valid() and perfil_form.is_valid():
			user_form.save()
			perfil_form.save()

	if request.user.first_name == '':
		context = {'user_form': user_form, 'perfil_form': perfil_form, }
		return render(request, 'registro_perfil.html', context)

	else:
		return render(request, 'muro.html')
		