from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

@api_view(http_method_names=['GET', 'PATCH', "DELETE"])
def agendamento_detail(request, id):
    if request.method != "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            v_data = serializer.validated_data
            serializer.save()
            return JsonResponse(v_data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        obj.delete()
        return Response(status=204)

@api_view(http_method_names=['GET', 'POST'])
def agendamento_list(request):
    if request.method == "GET":
        queryset = Agendamento.objects.all()
        serializer = AgendamentoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)