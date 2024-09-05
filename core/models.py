from django.db import models
from django.utils import timezone

class Pessoa(models.Model):
    nomeVoluntario = models.CharField(max_length=100)
    telefoneVoluntario = models.CharField(max_length=15)  
    emailVoluntario = models.EmailField(max_length=100) 
    enderecoVoluntario = models.CharField(max_length=100)
    funcaoVoluntario = models.CharField(max_length=100)
    dt_registro_voluntario = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nomeVoluntario