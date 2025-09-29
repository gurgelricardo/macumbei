from django.db import models

class Funcao(models.IntegerChoices):
    DEFUMACAO = 1, "Defumação"
    LIMPEZA = 2, "Limpeza"
    CORTE = 3, "Corte"
    DESCARREGO = 4, "Descarrego"
    DEFAULT = 5, "N/A"

class Linha(models.IntegerChoices):
    ASTRO = 1, "Astro"
    PRETO_VELHO = 2, "Preto velho"
    OGUM = 3, "Ogum"
    CABOCLO_DE_PENA = 4, "Caboclo de pena"
    MESTRES = 5, "Mestres"
    EXU = 6, "Exu"
    ERE = 7, "Erê"
    DEFAULT = 8, "N/A"

    