# Generated by Django 3.1.3 on 2020-11-12 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_agenda_foto_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='foto_perfil',
        ),
    ]