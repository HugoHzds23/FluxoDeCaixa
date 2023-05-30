from django.shortcuts import render, redirect
from django.contrib import auth, messages
from controlecaixa.forms import novocaixaForms
from controlecaixa import models
import datetime

def controlecaixa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login!")
        return redirect ('login') 
    return render(request, 'pedidos/listapedidos.html')



def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect ('login')



def novocaixa(request):
    forms = novocaixaForms(request.POST)
    if forms.is_valid():
        if models.novocaixa.objects.filter(hora_fechado__isnull=True):
            messages.error(request, "Ja possui um caixa aberto!")
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
    form = novocaixaForms(request.POST)
    if form.is_valid():
        if models.novocaixa.objects.filter(hora_fechado__isnull=True):
            models.novocaixa.objects.filter(hora_fechado__isnull=True).update(hora_fechado=datetime.datetime.now())
            messages.success(request, 'Caixa Fechado com Sucesso!')
            print (models.novocaixa.objects.filter())
            return redirect ('listadepedidos')
        else:
            messages.error(request,"Nao tem caixa aberto para ser Fechado, por favor abra um caixa!")
            return redirect('listadepedidos')

    return redirect ('listadepedidos')

