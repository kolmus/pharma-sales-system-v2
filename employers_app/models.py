from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    phone = models.BigIntegerField(verbose_name="Numer telefonu")
    role = models.CharField(max_length=128, verbose_name='Stanowisko')
    supervisor = models.ForeignKey('Employee', verbose_name='Przełożony', on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Zatrudniony')
    is_supervisor = models.BooleanField(default=False, verbose_name='Stanowisko kierownicze')
    
    @property
    def name(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    
    def __str__(self):
        return self.name

