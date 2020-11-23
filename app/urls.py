from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('Agenda', views.Dgenda, name='MinhaAgenda'),
    path('novoLembrete', views.lembrete, name='lembrete'),
    path('login', views.login, name="login"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('logout', views.logout, name="logout"),
    path('newlembrete', views.newlembrete, name="newlembrete"),
    path('deleta_lembrete/<int:agenda_id>', views.deleta_lembrete, name="deleta_lembrete"),
    path('calendario', views.calendario, name="calendario")
]
