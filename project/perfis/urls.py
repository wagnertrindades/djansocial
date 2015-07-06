from django.conf.urls import patterns, include, url
from django.contrib import admin
from project.perfis import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^perfis/(?P<perfil_id>\d+)$', views.showPerfil, name='showPerfil'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
)
