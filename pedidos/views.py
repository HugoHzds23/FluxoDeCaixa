from django.shortcuts import render, redirect
from django.contrib import messages
from pedidos.forms import novo_pedidoForms
from pedidos import models


# funcao de autenticação para permissao de acesso a pagina junto com autenticação de formulario 



def ad_pedidos(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login")
        return redirect ('login') 
    form = novo_pedidoForms(request.POST)
    if form.is_valid():
        contexto = {'form': form} 
        ped = form.save(commit=False)  
        ped.save()
        return redirect ('listadepedidos')
    contexto = {'form': form} 
    return render(request, 'pedidos/pedidos.html', contexto)
  
def listadepedidos (request):
    listapedidos = models.novo_pedido.objects.all()
    print (listapedidos)
    pedido = {'pedido' : listapedidos}
    return render (request, 'pedidos/listapedidos.html', pedido)