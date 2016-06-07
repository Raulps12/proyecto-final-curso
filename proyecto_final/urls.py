# -*- encoding: utf-8 -*-
"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from proyecto_final.aficionado.views import CountryAutocomplete, CityAutocomplete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('proyecto_final.aficionado.urls')),
    url(r'', include('proyecto_final.muro.urls')),
    url(r'', include('proyecto_final.evento.urls')),
    # Urls de Django-allauth
    url(r'^accounts/', include('allauth.urls')),
    # Urls de Cities-light
    url(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete',),
    url(r'^city-autocomplete/$', CityAutocomplete.as_view(), name='city-autocomplete',),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
