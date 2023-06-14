import datetime

from django.shortcuts import render, redirect
from django.contrib import auth, messages

from controlecaixa.forms import CaixaForms
from controlecaixa.models import Caixa


def controle_caixa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login!")
        return redirect ('login') 
    return render(request, 'pedidos/listapedidos.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect ('login')


def novo_caixa(request):
    forms = CaixaForms(request.POST)
    contexto = {'form':forms}
    if forms.is_valid():
        if Caixa.objects.filter(hora_fechado__isnull=True):
            messages.error(request, "Ja possui um caixa aberto!")
            return redirect ('listadepedidos')
        else:
            ped = forms.save()
            messages.success(request, "Caixa Aberto com Succeso!")
            return redirect ('listadepedidos')
    print(contexto)
    print(forms)
    return render (request, 'pedidos/listapedidos.html', contexto)


def lista_de_caixas(request):
    novoscaixas = Caixa.objects.all()
    print (novoscaixas)
    dados = {'novoscaixas' : novoscaixas}
    return render (request, 'controlecaixa/index2.html', dados)


def fechar_caixa(request):
    form = CaixaForms(request.POST)
    if form.is_valid():
        if Caixa.objects.filter(hora_fechado__isnull=True):
            Caixa.objects.filter(hora_fechado__isnull=True).update(hora_fechado=datetime.datetime.now())
            messages.success(request, 'Caixa Fechado com Sucesso!')
            print (Caixa.objects.filter())
            return redirect ('listadepedidos')
        else:
            messages.error(request,"Nao tem caixa aberto para ser Fechado, por favor abra um caixa!")
            return redirect('listadepedidos')
    return redirect ('listadepedidos')

