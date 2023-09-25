from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    modalidade = models.CharField(max_length=1,
                                   choices=(('P', 'Prestador'), ('C', 'Contratante')))
    nome_completo: models.CharField(max_length=50)
    data_nascimento: models.DateTimeField('%d-%m-%Y')
    cpf: models.CharField(max_length=11, unique=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    email = models.EmailField()
    


    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
