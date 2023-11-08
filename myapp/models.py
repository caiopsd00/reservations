from django.db import models

class Descricoes(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)