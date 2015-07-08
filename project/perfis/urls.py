from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('project.perfis.views',
	url(r'^$', 'indexPerfil', name='indexPerfil'),
    url(r'^(?P<perfil_id>\d+)$', 'showPerfil', name='showPerfil'),
    url(r'^(?P<perfil_id>\d+)/convidar$', 'convidar', name='convidar'),
)
