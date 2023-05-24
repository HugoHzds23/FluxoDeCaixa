from django.shortcuts import render, redirect
from django.contrib import auth, messages
from controlecaixa.forms import novocaixaForms
from controlecaixa import models
from django.http import HttpResponse


def controlecaixa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login")
        return redirect ('login') 
    return render(request, 'pedidos/listapedidos.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect ('login')


def novocaixa(request):
    forms = novocaixaForms(request.POST)
    if forms.is_valid():
        if models.novocaixa.objects.filter(hora_fechado__isnull=True):
            messages.error(request, "ja possui um caixa aberto!")
            return redirect ('listadepedidos')
        else:
            contexto = {'form':forms}
            ped = forms.save()
            messages.success(request, "Caixa Aberto com Succeso!")
            return redirect ('listadepedidos')
            
    return render (request, 'controlecaixa/index.html')


def listadecaixas(request):
    novoscaixas = models.novocaixa.objects.all()
    print (novoscaixas)
    dados = {'novoscaixas' : novoscaixas}
    return render (request, 'controlecaixa/index2.html', dados)

def fecharcaixa(request):
    if models.novocaixa.objects.filter(hora_fechado__isnull=True):
        caixa_atualizar = models.novocaixa.objects.get(hora_fechado=models.novocaixa.objects.last().id_caixa)
        caixa_atualizar.hora_fechado


 