from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'project.core.views.index', name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'project.core.views.showPerfil', name='showPerfil'),
)
