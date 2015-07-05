from django.db import models
from django.utils import timezone

class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)
	dtNascimento = models.CharField(max_length=10, null=False)
	localidade = models.CharField(max_length=255, null=True)
	cargo = models.CharField(max_length=155, null=True)
	empresa = models.CharField(max_length=155, null=True)
	curso = models.CharField(max_length=155, null=True)
	escola = models.CharField(max_length=155, null=True)
	dtCadastro = models.DateTimeField(editable=False, default=timezone.now) 
