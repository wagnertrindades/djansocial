from django.db import models

class Perfil(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    foto = models.ImageField(
        upload_to='perfis/images', verbose_name='Foto', null=True, blank=True
    )
    dtNascimento = models.CharField('Data de Nascimento', max_length=10)
    localidade = models.CharField('Localidade', max_length=255, blank=True)
    cargo = models.CharField('Cargo', max_length=155, null=True, blank=True)
    empresa = models.CharField('Empresa', max_length=155, null=True, blank=True)
    curso = models.CharField('Curso', max_length=155, null=True, blank=True)
    escola = models.CharField('Escola', max_length=155, null=True, blank=True)
    dtCadastro = models.DateTimeField('Criado em', auto_now_add=True)
    dtAtualizacao = models.DateTimeField('Atualizado em', auto_now=True)
    
    def __str__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return ('perfis:showPerfil', (), { 'perfil_id' : self.id })

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        ordering = ['nome']

    def convidar(self, perfil_convidado):
        Convite(solicitante=self, convidado=perfil_convidado).save()

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')