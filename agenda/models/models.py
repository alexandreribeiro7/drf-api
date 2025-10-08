from django.db import models
from django.contrib.auth.models import User


class Agendamento(models.Model):
    prestador = models.ForeignKey('auth.User', related_name='agendamentos', on_delete=models.CASCADE)
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=15)


class Endereco(models.Model):
    prestador = models.ForeignKey(User, related_name='enderecos', on_delete=models.CASCADE)
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, blank=True, null=True)
