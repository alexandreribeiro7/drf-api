from django.utils import timezone
from rest_framework import serializers

from agenda.models.models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['id', 'data_horario', 'nome_cliente', 'email_cliente', 'telefone_cliente']
        read_only_fields = ['id']
    
    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data e horário não podem ser no passado.")
        return value
    
    def validate(self, attrs):
        telefone_cliente = attrs.get('telefone_cliente', "")
        email_cliente = attrs.get('email_cliente', "")
        
        if email_cliente.endswith('.br') and telefone_cliente.startswith('+') and not telefone_cliente.startswith('+55'):
            raise serializers.ValidationError("E-mail brasileiro deve estar associado a um telefone brasileiro.")
        return attrs