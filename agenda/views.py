from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

@api_view(http_method_names=['GET', 'PATCH'])
def agendamento_detail(request, id):
    if request.method != "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            v_data = serializer.validated_data
            obj.data_horario = v_data.get('data_horario', obj.data_horario)
            obj.nome_cliente = v_data.get('nome_cliente', obj.nome_cliente)
            obj.email_cliente = v_data.get('email_cliente', obj.email_cliente)
            obj.telefone_cliente = v_data.get('telefone_cliente', obj.telefone_cliente)
            obj.save()
            return JsonResponse(v_data, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=['GET', 'POST'])
def agendamento_list(request):
    if request.method == "GET":
        queryset = Agendamento.objects.all()
        serializer = AgendamentoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            existe = Agendamento.objects.filter(
                data_horario=validated_data['data_horario'],
                nome_cliente=validated_data['nome_cliente'],
                email_cliente=validated_data['email_cliente'],
                telefone_cliente=validated_data['telefone_cliente']
            ).exists()
            if existe:
                return JsonResponse({"error": "Agendamento já existe"}, status=400)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)