from django.contrib import admin
from app.models import Agenda

admin.site.register(Agenda)
class siteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_lembrete', 'pessoa')
    list_filter = ('date_lembrete')
    search_fields = ('titulo', 'date_lembrete')