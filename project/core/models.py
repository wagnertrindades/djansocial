from django.db import models

class Perfil(object):

	def __init__(self, foto='', nome='', email='', dtNascimento='', localidade='', cargo='', empresa='', curso='', escola=''):
		self.nome = nome
		self.email = email
		self.dtNascimento = dtNascimento
		self.localidade = localidade
		self.cargo = cargo
		self.empresa = empresa
		self.curso = curso
		self.escola = escola
