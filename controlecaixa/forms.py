from django import forms
from controlecaixa.models import novocaixa

class novocaixaForms(forms.ModelForm):
    class Meta:
        model = novocaixa
        fields = '__all__'