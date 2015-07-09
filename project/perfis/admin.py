from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'dtNascimento']
    search_fields = ['nome', 'email']

admin.site.register(Perfil, PerfilAdmin)

