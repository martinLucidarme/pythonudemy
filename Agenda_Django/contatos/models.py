from django.db import models
from django.utils import timezone


# Create your models here.
# When model is made, or after any modification: python manage.py makemigrations
# then python manage.py migrate

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome  # para aparecer o nome da categoria criada


class Contato(models.Model):
    nome = models.CharField(max_length=255)  # tudo que é Field é um campo
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
