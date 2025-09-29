from django.db import models
from .enums import Linha, Funcao
from django.utils.text import slugify

def audio_path(instance, filename):
    extensao = filename.split('.')[-1]

    titulo_slug = slugify(instance.nome)

    return f'audios/{titulo_slug}.{extensao}'

class Ponto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(null=False, blank=False, max_length=100)
    funcao = models.PositiveSmallIntegerField(choices=Funcao.choices, default=Funcao.DEFAULT,)
    linha = models.PositiveSmallIntegerField(choices=Linha.choices, default=Linha.DEFAULT)
    entidade = models.CharField(null=True, max_length=20, blank=True)
    letra = models.TextField(null=False, blank=False, max_length=777)
    link_audio = models.FileField(upload_to=audio_path)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
