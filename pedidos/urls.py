from django.urls import path
from .views import novo_pedido, lista_de_pedidos_e_despesas, editar_pedido, deletar_pedido, nova_despesa, deletar_despesa, editar_despesas

urlpatterns = [
    path('novopedido', novo_pedido, name='novo_pedido'),
    path('listapedidos', lista_de_pedidos_e_despesas, name='listadepedidos'),
    path('update/<int:pk>', editar_pedido, name='editarpedido'),
    path('delete/<int:pk>', deletar_pedido, name='deletarpedido'),
    path('despesas', nova_despesa, name='despesas'),
    path('deletedespesa/<int:pk>', deletar_despesa, name='deletadespesa'),
    path('editardespesa/<int:pk>', editar_despesas, name='editar_despesas')
]   