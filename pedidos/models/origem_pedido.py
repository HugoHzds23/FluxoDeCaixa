from django.db import models
from django.utils.translation import gettext_lazy as _


# models para origem do cliente para colocar no formulario
class origem_pedido(models.TextChoices):
    IFOOD = 'IFOOD', _('ifood')
    BALCAO = 'BALCAO', _('Balcao')
    TELEFONE = 'TELEFONE', _('Telefone')
    WHATSAAP = 'WHATSAAP', _('WhatSaap')

