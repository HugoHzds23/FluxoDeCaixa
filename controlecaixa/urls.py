from django.urls import path
from controlecaixa.views import controle_caixa, logout, novo_caixa, lista_de_caixas,fechar_caixa

urlpatterns = [
    path ('caixa', controle_caixa, name='controlecaixa'),
    path ('logout', logout, name ="logout"),
    path ('novocaixa', novo_caixa, name='novocaixa'),
    path ('fecharcaixa', fechar_caixa, name='fecharcaixa'),
    path ('listadecaixas', lista_de_caixas, name='listadecaixas')
] 