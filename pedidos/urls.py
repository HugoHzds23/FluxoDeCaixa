from django.urls import path
from .views import ad_pedidos, listadepedidos, editarpedidos, deletarpedido

urlpatterns = [
    path('novopedido', ad_pedidos, name='novo_pedido'),
    path('listapedidos', listadepedidos, name='listadepedidos'),
    path('update/<int:pk>', editarpedidos, name='editarpedido'),
    path('delete/<int:pk>', deletarpedido, name='deletarpedido')
]   