from django.db import models
from django.utils.translation import gettext_lazy as _


# models para origem do cliente para colocar no formulario
class origem_pedido(models.TextChoices):
    IFOOD = 'IFOOD', _('IFOOD')
    BALCAO = 'BALCAO', _('BALCAO')
    TELEFONE = 'TELEFONE', _('TELEFONE')
    WHATSAPP = 'WHATSAPP', _('WHATSAPP')


class Pedido(models.Model):
    origem_pedido = models.TextField(choices=origem_pedido.choices, max_length=50)
    id_ifood = models.CharField(null=False, max_length=20 , blank=True)
    cliente = models.CharField(max_length=100)
    dinheiro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
    cartao_credito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
    cartao_debito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
    pix =   models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
    observacoes =   models.CharField(max_length=200, blank=True)


class Despesa(models.Model):
    tipo_despesa = models.CharField(max_length=30)
    nome_motoboy = models.CharField(max_length=50)
    valor_dinheiro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
    valor_pix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default='0')
