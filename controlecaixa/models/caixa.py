from django.db import models

#criando formulario para abrir e fechar caixa
class novocaixa(models.Model):
    id_caixa = models.AutoField(primary_key=True)
    hora_aberto = models.DateTimeField(auto_now=True)
    hora_fechado =  models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return self.id_caixa