from django.db import models

class Carros(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    foto = models.ImageField(upload_to="produtos")
    descricao = models.CharField(max_length=200)

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    celular = models.CharField(max_length=15, default='0000')
    genero = models.CharField(max_length=25, default='')
