from django.db import models

from pedidos.models import Pedido

class Caixa(models.Model):
    hora_aberto = models.DateTimeField(auto_now_add=True)
    hora_fechado =  models.DateTimeField(null=True, blank=True)


    def soma_dinheiro():
        pass


    def soma_cartao_credito():
        pass


    def soma_cartao_debito():
        pass


    def soma_pix():
        pass


    def soma_pedidos_ifood():
        pass 


    def soma_pedidos_whatssap():
        pass 


    def soma_pedidos_balcao():
        pass 

    def soma_pedidos_telefone():
        pass 