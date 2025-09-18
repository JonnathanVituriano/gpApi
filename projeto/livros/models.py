from django.db import models

# Create your models here.

class LivroModel(models.Model):
    titulo = models.CharField(max_length=250)

    def __str__(self):
        return self.titulo