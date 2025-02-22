# Generated by Django 5.0.6 on 2024-06-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_experiencia_entrenador_horas_entrenadas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrenador',
            name='horas_entrenadas',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='posicion',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('jugador', 'Jugador'), ('entrenador', 'Entrenador')], max_length=20),
        ),
    ]
