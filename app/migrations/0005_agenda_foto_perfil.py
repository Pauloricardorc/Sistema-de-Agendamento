# Generated by Django 3.1.3 on 2020-11-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_agenda_foto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%m/%y/'),
        ),
    ]
