# Generated by Django 5.0.6 on 2024-06-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_entrenador_jugador_alter_myuser_user_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrenador',
            old_name='experiencia',
            new_name='horas_entrenadas',
        ),
        migrations.RemoveField(
            model_name='entrenador',
            name='especialidad',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('entrenador', 'Entrenador'), ('jugador', 'Jugador')], max_length=20),
        ),
    ]
