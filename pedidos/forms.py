from django import forms
from pedidos.status_do_pedido import status_pedido
from pedidos.origem_pedido import origem_pedido

class novo_pedido(forms.Form):
    ID = forms.IntegerField(
        widget = forms.NumberInput(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite o id do Ifood"
                        }
    
                )
    )

    status = forms.ChoiceField(
        label='Status do Pedido',
        choices=status_pedido,
                widget = forms.Select(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite nome do cliente"
                        }
    
                )
    )
    
    origem = forms.ChoiceField(
        label='Origem do Pedido',
        choices=origem_pedido,
                widget = forms.Select(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite nome do cliente"
                        }
    
                )
    )
    
    cliente = forms.CharField(
        max_length=100,
        widget = forms.TextInput(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite nome do cliente"
                        }
    
                )
    )
    dinheiro = forms.IntegerField(
                widget = forms.NumberInput(
                       attrs = {
                                "class": "form-inline -col",
                                "placeholder": "Dinheiro"
                        }
    
                )
    )
    cartao_credito = forms.IntegerField(
                widget = forms.NumberInput(
                       attrs = {
                                "class": "form-inline -col",
                                "placeholder": "Credito"
                        }
    
                )
    )
    cartao_debito = forms.IntegerField(
                widget = forms.NumberInput(
                       attrs = {
                                "class": "form-inline -col",
                                "placeholder": "Debito"
                        }
    
                )
    )
    pix = forms.IntegerField(
                widget = forms.NumberInput(
                       attrs = {
                                "class": "form-inline -pix",
                                "placeholder": "PIX"
                        }
    
                )
    )


    Observacoes = forms.CharField(
        label='Observações',
                widget = forms.Textarea(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite nome do cliente"
                        }
    
                )
    )
    

def clean_cliente(self):
        cliente = self.cleaned_data('origem').get
        if any(char.isdigit()for char in cliente):
              raise forms.ValidationError("Cliente Invalida: Não incluir numero no nome do cliente")
        else:
              return cliente
