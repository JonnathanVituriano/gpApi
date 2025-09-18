from django.db import models

# Create your models here.

class LivroModel(models.Model):
    titulo = models.CharField(max_length=250)
    nome_autor = models.CharField(max_length=250)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo