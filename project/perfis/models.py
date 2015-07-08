from django.db import models
from django.utils import timezone

class Perfil(models.Model):

	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')
	email = models.CharField('E-mail', max_length=100)
	dtNascimento = models.DateField('Data de Nascimento')
	localidade = models.CharField('Localidade',max_length=255, blank=True)
	cargo = models.CharField('Cargo', max_length=155, null=True)
	empresa = models.CharField('Empresa', max_length=155, null=True)
	curso = models.CharField('Curso', max_length=155, null=True)
	escola = models.CharField('Escola', max_length=155, null=True)
	dtCadastro = models.DateTimeField('Criado em', auto_now_add=True)
	dtAtualizacao = models.DateTimeField('Atualizado em', auto_now=True) 

	def __str__(self):
		return self.name

	def convidar(self, perfil_convidado):
		Convite(solicitante = self, convidado = perfil_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
	convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

