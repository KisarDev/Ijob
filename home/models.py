from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    modalidade = models.CharField(max_length=1,
                                   choices=(('P', 'Prestador'),
                                            ('C', 'Contratante')))
    nome_completo = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    


    