from django.urls import path
from controlecaixa.views import controlecaixa, logout, novocaixa, listadecaixas,fecharcaixa

urlpatterns = [
    path ('caixa', controlecaixa, name='controlecaixa'),
    path ('logout', logout, name ="logout"),
    path ('novocaixa', novocaixa, name='novocaixa'),
    path ('fecharcaixa', fecharcaixa, name='fecharcaixa'),
    path ('listadecaixas', listadecaixas, name='listadecaixas')
]