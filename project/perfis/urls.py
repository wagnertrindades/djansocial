from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^perfis/(?P<perfil_id>\d+)$', 'project.perfis.views.showPerfil', name='showPerfil'),
)
