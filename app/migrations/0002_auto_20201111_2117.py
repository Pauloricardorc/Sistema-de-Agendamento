# Generated by Django 3.1.3 on 2020-11-12 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='foto_receita',
            new_name='foto_perfil',
        ),
    ]
