from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('Agenda', views.Agenda, name='MinhaAgenda'),
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro")
]
