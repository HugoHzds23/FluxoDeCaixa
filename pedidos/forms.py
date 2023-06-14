from django import forms
from pedidos.models import Pedido, Despesa


#criando formulario com base no ModelForm que foi criando na pasta models
class PedidoForms(forms.ModelForm):
      class Meta:
            model = Pedido
            fields = ['origem_pedido', 'id_ifood', 'cliente', 'dinheiro', 'cartao_credito', 'cartao_debito', 'pix', 'observacoes']
            widgets = {
                'class': 'form-group'
          }
 

class DespesaForms(forms.ModelForm):
      class Meta:
            model = Despesa
            fields = ['tipo_despesa', 'nome_motoboy', 'valor_dinheiro', 'valor_pix']
            widgets = {
                'class': 'form-group'
          }