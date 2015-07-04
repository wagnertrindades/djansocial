from django.shortcuts import render
from project.core.models import Perfil 

def index(resquest):
	return render(resquest, 'core/index.html')

def showPerfil(resquest, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)
	return render(resquest, 'core/perfis.html', { 'perfil' : perfil })