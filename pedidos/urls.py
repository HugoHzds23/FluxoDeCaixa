from django.urls import path
from .views import ad_pedidos

urlpatterns = [
    path('novopedido', ad_pedidos, name='novo_pedido')
]   