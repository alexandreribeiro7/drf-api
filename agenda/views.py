from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

@api_view(http_method_names=['GET'])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(obj)
    return JsonResponse(serializer.data)

@api_view(http_method_names=['GET'])
def agendamento_list(request):
    queryset = Agendamento.objects.all()
    serializer = AgendamentoSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)