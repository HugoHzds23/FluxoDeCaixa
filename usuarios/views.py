from django.shortcuts import render, redirect
from usuarios.forms import loginforms, cadastroforms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = loginforms()

    if request.method == "POST":
        form = loginforms(request.POST)
        
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        
        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f"{nome} logado com sucesso")
            return redirect ('controlecaixa')
        else:
            messages.error(request, "Erro ao efetuar o Login")
            return redirect ('login')



    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = cadastroforms()
    
    if request.method == "POST":
        form = cadastroforms(request.POST)

        if form.is_valid():
             if form["senha_1"].value() != form["senha_2"].value():
                messages.error (request, "as duas senha digitadas nao conferem")
                return redirect ('cadastro')
             
             nome=form["nome_cadastro"].value()
             email=form["email"].value()
             senha=form["senha_1"].value()

             if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario ja existente")
                return redirect('cadastro')
             
             usuario = User.objects.create_user(
                 username = nome,
                 email = email,
                 password = senha,
             )
             usuario.save()
             messages.success(request, "Usuario Cadastrado")
             return redirect('login')






    return render(request, 'usuarios/cadastro.html', {'form': form})


