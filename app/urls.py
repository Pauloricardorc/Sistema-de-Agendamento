from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('agenda', views.Agenda, name='MinhaAgenda')
]
