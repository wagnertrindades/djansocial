from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('project.perfis.views',
	url(r'^$', 'showPerfis', name='showPerfis'),
    url(r'^(?P<perfil_id>\d+)$', 'index', name='index'),
    url(r'^(?P<perfil_id>\d+)/convidar$', 'convidar', name='convidar'),
)
