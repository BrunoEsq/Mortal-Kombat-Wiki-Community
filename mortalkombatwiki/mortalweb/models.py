from django.db import models
from django.core.validators import MinLengthValidator

class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    biography = models.TextField(validators=[MinLengthValidator(1000)], default='Biografía por defecto', max_length=1600)
    introduction = models.TextField(validators=[MinLengthValidator(200)], default='Introducción por defecto', max_length=400)
    imagen_titulo = models.ImageField(upload_to='')
    imagen_personaje = models.ImageField(upload_to='')
    imagen_fondo = models.ImageField(upload_to='')
    video1 = models.CharField(max_length=400, blank=True, null=True)
    video2 = models.CharField(max_length=400, blank=True, null=True)
    video3 = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.nombre


    # audio = models.FileField(upload_to='mortalweb/static/audio')


class Character(models.TextChoices):
    SCORPION = 'Scorpion', 'Scorpion'
    SUB_ZERO = 'Sub-Zero', 'Sub-Zero'
    LIU_KANG = 'Liu Kang', 'Liu Kang'
    RAIDEN = 'Raiden', 'Raiden'
    JOHNNY_CAGE = 'Johnny Cage', 'Johnny Cage'
    SHAO_KANG = 'Shao Kahn', 'Shao Kahn'
    OMNIMAN = 'Omniman', 'Omniman'
    KUNG_LAO = 'Kung Lao', 'Kung Lao'
    REPTILE = 'Reptile', 'Reptile'
    SMOKE = 'Smoke', 'Smoke'
    LI_MEI = 'Li Mei', 'Li Mei'
    ASHRAH = 'Ashrah', 'Ashrah'
    KENSHI = 'Kenshi', 'Kenshi'
    NITARA = 'Nitara', 'Nitara'
    GERAS = 'Geras', 'Geras'
    HAVIK = 'Havik', 'Havik'
    KITANA = 'Kitana', 'Kitana'
    MILEENA = 'Mileena', 'Mileena'
    RAIN = 'Rain', 'Rain'
    SINDEL = 'Sindel', 'Sindel'

class Coaching(models.Model):
    nombre = models.CharField(max_length=12)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=50)
    personaje = models.CharField(max_length=20, choices=Character.choices, default=Character.MILEENA)
    rank = models.CharField(max_length=6)
    city = models.CharField(max_length=10)


class Contact(models.Model):
    email = models.EmailField()
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    favorite_game = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

class CharacterRequest(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    introduction = models.TextField()
    title_image = models.ImageField(upload_to='images/')
    character_image = models.ImageField(upload_to='images/')
    background_image = models.ImageField(upload_to='images/')
    video1 = models.CharField(max_length=400, blank=True, null=True)
    video2 = models.CharField(max_length=400, blank=True, null=True)
    video3 = models.CharField(max_length=400, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre