from django.shortcuts import render
from project.perfis.models import Perfil

def showPerfis(resquest):
    perfis = Perfil.objects.all()
    template_name = 'perfis/perfis.html'
    context =  { 
        'perfis' : perfis 
    }
    return render(resquest, template_name, context)

def index(resquest, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    template_name = 'perfis/index.html'
    context = {
        'perfil' : perfil
    }
    return render(resquest, template_name, context)

def convidar(resquest, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(resquest)
    perfil_logado.convidar(perfil_a_convidar)

def get_perfil_logado(resquest):
    return Perfil.objects.get(id=1)