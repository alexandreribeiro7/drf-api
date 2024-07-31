from rest_framework import serializers


class AgendamentoSerializer(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length=200)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length=20)