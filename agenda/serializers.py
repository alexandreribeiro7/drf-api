from rest_framework import serializers

from agenda.models import Agendamento

class AgendamentoSerializer(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length=100)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length=15)
    
    def create(self, validated_data):
        return Agendamento.objects.create(**validated_data)