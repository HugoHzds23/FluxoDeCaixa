from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def controlecaixa(request):
    if not request.user.is_authenticated:
        messages.error(request, "Voce não esta logado, por favor faça o Login")
        return redirect ('login')      
    return render (request, 'controlecaixa/index.html') 

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect ('login')
