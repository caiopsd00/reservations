from django.db import models

class Descricoes(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)

class Usuario(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    administrador = models.BooleanField()

class Diaria(models.Model):
    dia = models.DateField()
    disponibilidade = models.BooleanField()
    preco = models.FloatField()
    hospede = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True,  default=None)