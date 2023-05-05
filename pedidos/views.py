from django.shortcuts import render, redirect
from django.contrib import messages
from pedidos.forms import novo_pedido



def ad_pedidos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login")
        return redirect ('login') 
    form = novo_pedido()
    contexto = {'form': form}     
    return render(request, 'pedidos/pedidos.html', contexto)
