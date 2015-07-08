from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('project.core.views',
    url(r'^$', 'index', name='index'),
)