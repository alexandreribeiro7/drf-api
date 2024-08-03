from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
@api_view(http_method_names=["GET", "PUT"])
def agendamento_detail(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PUT":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data_horario = validated_data.get("data_horario", obj.data_horario)
            obj.name_cliente = validated_data.get("name_cliente", obj.name_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method == "GET":
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Agendamento.objects.create(
                data_horario=validated_data["data_horario"],
                name_cliente=validated_data["name_cliente"],
                email_cliente=validated_data["email_cliente"],
                telefone_cliente=validated_data["telefone_cliente"],
            )
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)