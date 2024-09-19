from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, user_type=None, first_name=None, last_name=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario es obligatorio')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, user_type=None, first_name=None, last_name=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, email=email, password=password, user_type=user_type, first_name=first_name, last_name=last_name, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('jugador', 'Player'),
        ('entrenador', 'Coach'),
    )

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'user_type']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user_type == 'jugador' and not hasattr(self, 'player'):
            Player.objects.create(user=self)
        elif self.user_type == 'entrenador' and not hasattr(self, 'coach'):
            Coach.objects.create(user=self)

class Player(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Player: {self.user.username}"

    class Meta:
        db_table = 'accounts_player'


class Coach(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Coach: {self.user.username}"

    class Meta:
        db_table = 'accounts_coach'
