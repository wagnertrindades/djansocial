from django.db import models

class Perfil(object):

	def __init__(self, nome='', email=''):
		self.nome = nome
		self.email = email
