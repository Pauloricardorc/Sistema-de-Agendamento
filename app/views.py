from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('MinhaAgenda')
    return render(request, 'index.html')

def Agenda(request):
    return render(request, 'MinhaAgenda.html')

def cadastro(request):
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        user = User.objects.create_user(username=name, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'Cadastro.html')

def login(request):
    return render(request, 'index.html')

def logout(request):
    pass