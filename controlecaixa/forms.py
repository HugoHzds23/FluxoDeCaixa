from django import forms
from controlecaixa.models import Caixa

class CaixaForms(forms.ModelForm):
    class Meta:
        model = Caixa
        fields = '__all__'