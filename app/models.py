from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Agenda(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    lembrete = models.CharField(max_length=50)
    date_lembrete = models.DateTimeField(default=datetime.now, blank=True)
    feito = models.BooleanField(default=False)
