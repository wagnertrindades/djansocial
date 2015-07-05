from django.shortcuts import render
from project.perfis.models import Perfil

def index(resquest):

	allPerfis = Perfil.objects.all()
	return render(resquest, 'core/index.html', { 'perfis' : allPerfis })