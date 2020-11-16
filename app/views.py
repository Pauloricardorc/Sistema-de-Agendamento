from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from app.models import Agenda
       
# Create your views here.

def index(request):
    if request.method == "POST":
        email = request.POST['email']
        senha = request.POST['senha']
        print("Era pra Funcionar")
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('MinhaAgenda')
    return render(request, 'index.html')

def Dgenda(request):
    if request.user.is_authenticated:
        id = request.user.id
        agenda = Agenda.objects.order_by('-date_lembrete').filter(pessoa=id)
        dados = {
            'agenda' : agenda
        }
        print(dados)
        return render(request, 'MinhaAgenda.html', dados)
    else:
        return redirect('Home')

def cadastro(request):
    if request.method == "POST":
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
    auth.logout(request)
    return redirect('Home')

def lembrete(request):
    return render(request, 'criar_na_agenda.html')

def newlembrete(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        lembrete = request.POST['lembrete']
        date_lembrete = request.POST['data_cadastro']
        user = get_object_or_404(User, pk=request.user.id)
        agenda = Agenda.objects.create(pessoa=user, titulo=titulo, lembrete=lembrete, date_lembrete=date_lembrete)
        agenda.save()
        return redirect('MinhaAgenda')
    else:
        print('?')
        return render(request, 'criar_na_agenda.html')

def deleta_lembrete(request, agenda_id):
    agenda = get_object_or_404(Agenda, pk=agenda_id)   
    agenda.delete()
    return redirect('MinhaAgenda')