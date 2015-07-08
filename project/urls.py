from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('project.core.urls', namespace='core')),
    url(r'^perfis/', include('project.perfis.urls', namespace='perfis')),
    url(r'^admin/', include(admin.site.urls)),
)
