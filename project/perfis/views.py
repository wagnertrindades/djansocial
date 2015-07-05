from django.shortcuts import render
from project.perfis.models import Perfil 

def showPerfil(resquest, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)
	return render(resquest, 'perfis/perfis.html', { 'perfil' : perfil })