#
from django.db import models
from veiculo.consts import *


class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)

    def __str__(self):
        return '{0} - {1} ({2} / {3})'.format(
            self.get_marca_display(),
            self.modelo,
            self.ano,
            self.get_cor_display()
        )