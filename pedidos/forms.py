from django import forms
from pedidos.models import novo_pedido, origem_pedido


#criando formulario com base no ModelForm que foi criando na pasta models
class novo_pedidoForms(forms.ModelForm):
    class Meta:
          model = novo_pedido
          fields = '__all__'
          widgets = {
                'class': 'form-group'
          }