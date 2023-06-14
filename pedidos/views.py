from django.shortcuts import render, redirect
from django.contrib import messages


from pedidos.forms import PedidoForms, DespesaForms
from pedidos.models import Pedido , Despesa
from controlecaixa.models import Caixa


#--------------------------------------
#função para adicoonar pedidos
# #-------------------------------------- 
def novo_pedido(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    form = PedidoForms(request.POST)
    contexto = {'form':form}
    if form.is_valid():
        contexto = {'form': form} 
        ped = form.save()
        ped.save()
        return redirect ('listadepedidos')
    return render(request, 'pedidos/pedidos.html', contexto)
  

#--------------------------------------
#função para editar pedidos 
#--------------------------------------
def editar_pedido(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    pedido = Pedido.objects.get(pk=pk)
    form = PedidoForms(request.POST or None, instance=pedido)
    if form.is_valid():
        contexto = {'form': form} 
        ped = form.save(commit=False)  
        ped.save()
        return redirect ('listadepedidos')
    contexto = {'form': form} 
    return render(request, 'pedidos/pedidos.html', contexto)


#--------------------------------------
#função para deletar pedidos 
#--------------------------------------
def deletar_pedido(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    pedido = Pedido.objects.get(pk=pk)
    pedido.delete()
    return redirect('listadepedidos')


#--------------------------------------
#função para adicoonar despesas 
#--------------------------------------
def nova_despesa(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    form_despesa = DespesaForms(request.POST)
    if form_despesa.is_valid():
        contexto = {'form': form_despesa}
        des = form_despesa.save(commit=False)
        des.save()
        return redirect ('listadepedidos')
    contexto = {'form': form_despesa}
    return render (request, 'pedidos/despesas.html', contexto)


#--------------------------------------
#função para exibir lista de pedidos e despesas 
# #-------------------------------------- 
def lista_de_pedidos_e_despesas(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login')    
    Pedidos = Pedido.objects.all()
    Despesas = Despesa.objects.all()
    print(Pedidos)
    print(Despesas)
    pedido = {'pedido' : Pedidos, 'despesa': Despesas}
    return render(request, 'pedidos/listapedidos.html', pedido)


#--------------------------------------
#função de deletar despesa
#--------------------------------------
def deletar_despesa(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    despesa = Despesa.objects.get(pk=pk)
    despesa.delete()
    return redirect('listadepedidos')


#--------------------------------------
#função de deletar despesa
#--------------------------------------
def editar_despesas(request,pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Voce não esta logado, por favor faça o Login')
        return redirect ('login') 
    pedido = Despesa.objects.get(pk=pk)
    form = DespesaForms(request.POST or None, instance=pedido)
    if form.is_valid():
        contexto = {'form': form} 
        ped = form.save(commit=False)  
        ped.save()
        return redirect ('listadepedidos')
    contexto = {'form': form} 
    return render(request, 'pedidos/despesas.html', contexto)