from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Agenda(request):
    return render(request, 'MinhaAgenda.html')