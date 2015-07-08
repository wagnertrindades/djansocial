from django.shortcuts import render
from project.perfis.models import Perfil 

def indexPerfil(resquest):
	allPerfis = Perfil.objects.all()
	return render(resquest, 'perfis/index.html', { 'perfis' : allPerfis })

def showPerfil(resquest, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	return render(resquest, 'perfis/perfis.html', { 'perfil' : perfil })

def convidar(resquest, perfil_id):
	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(resquest)
	perfil_logado.convidar(perfil_a_convidar)

def get_perfil_logado(resquest):
	return Perfil.objects.get(id=1)