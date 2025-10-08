from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.models import User

from agenda.models.models import Agendamento, Endereco
from agenda.utils import get_horarios_disponiveis

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
        
        prestador = serializers.CharField()
        
        def validate_prestador(self, value):
            try:
                prestador_obj = User.objects.get(username=value)
            except User.DoesNotExist:
                raise serializers.ValidationError("Prestador não encontrado.")
            return prestador_obj
    
    def validate_data_horario(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data e horário não podem ser no passado.")
        if value not in get_horarios_disponiveis(value.date()):
            raise serializers.ValidationError("Horário já agendado.")
        return value
    
    def validate(self, attrs):
        telefone_cliente = attrs.get('telefone_cliente', "")
        email_cliente = attrs.get('email_cliente', "")
        
        if email_cliente.endswith('.br') and telefone_cliente.startswith('+') and not telefone_cliente.startswith('+55'):
            raise serializers.ValidationError("E-mail brasileiro deve estar associado a um telefone brasileiro.")
        return attrs


class EndereçoSerializer(serializers.Serializer):
    cep = serializers.CharField(max_length=10, required=True)
    estado = serializers.CharField(max_length=50, required=True)
    cidade = serializers.CharField(max_length=100, required=True)
    rua = serializers.CharField(max_length=200, required=True)
    complemento = serializers.CharField(max_length=200, required=False, allow_blank=True)

    
class PrestadorSerializer(serializers.ModelSerializer):
    agendamentos = AgendamentoSerializer(many=True, read_only=True)
    enderecos = EndereçoSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'agendamentos', 'enderecos']
        
    
class CriarEnderecoParaPrestadorSerializer(serializers.Serializer):
    endereco = EndereçoSerializer()

    def create(self, validated_data):
        endereco_data = validated_data['endereco']
        prestador = self.context.get('prestador')
        if Endereco.objects.filter(prestador=prestador).exists():
            raise serializers.ValidationError("Este prestador já possui um endereço cadastrado.")
        return Endereco.objects.create(prestador=prestador, **endereco_data)

