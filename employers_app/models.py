from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    phone = models.BigIntegerField(verbose_name="Numer telefonu")
    role = models.CharField(max_length=128, verbose_name="Stanowisko")
    supervisor = models.ForeignKey("Employee", verbose_name="Przełożony", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Zatrudniony")
    is_supervisor = models.BooleanField(default=False, verbose_name="Stanowisko kierownicze")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



