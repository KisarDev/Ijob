from django.db import models

class Profissao(models.Model):
    profissao = models.CharField(max_length=255)
    tempo_experiencia = models.CharField(max_length=255)
    preco_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='fotos/')  
    
    def __str__(self):
        return self.profissao
