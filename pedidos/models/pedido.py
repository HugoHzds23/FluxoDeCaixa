from django.db import models
from .origem_pedido import origem_pedido

#models para cadastro de pedido para adicionar no caixa
class novo_pedido(models.Model):
    origempedido    =   models.TextField(choices=origem_pedido.choices, max_length=50)
    id_ifood        =   models.CharField(null=False, max_length=20 , blank=True)
    cliente         =   models.CharField(max_length=100)
    dinheiro        =   models.FloatField(null=True,default='0', blank=True)
    cartao_credito  =   models.FloatField(null=True,default='0', blank=True)
    cartao_debito   =   models.FloatField(null=True,default='0', blank=True)
    pix             =   models.FloatField(null=True,default='0', blank=True)
    Observacoes     =   models.CharField(max_length=200, blank=True)