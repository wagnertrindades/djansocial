from django.shortcuts import render
from project.core.models import Perfil 

def index(resquest):
	return render(resquest, 'core/index.html')

def showPerfil(resquest, perfil_id):
	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil(nome='Steve Vai', email='steve@vai.com', dtNascimento='10/05/1978', localidade='EUA', cargo='Guitarrista', empresa='Steve Vai', curso='Arpegios', escola='Malmsteen School' )

	return render(resquest, 'core/perfis.html', { 'perfil' : perfil })