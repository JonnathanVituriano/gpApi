from django.db import models
from django.core.validators import RegexValidator

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    telefone = models.CharField(
        unique=True,
        max_length=11,
        validators=[
            RegexValidator(
                regex=r'^\d{2}9\d{8}$',
                message= 'número inválido! Use o formato DDD + 9 + número ',
                code = 'invalid_telefone'
            )
        ]
    )


    def __str__(self):
        return self.nome
