from django.urls import path
from .views import ad_pedidos, listadepedidos

urlpatterns = [
    path('novopedido', ad_pedidos, name='novo_pedido'),
    path('listapedidos', listadepedidos, name='listadepedidos')
]   