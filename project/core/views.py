from django.shortcuts import render
from project.perfis.models import Perfil

def index(resquest):
	return render(resquest, 'core/index.html')