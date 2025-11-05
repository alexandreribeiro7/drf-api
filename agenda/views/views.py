import csv
from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import permissions
from django.contrib.auth.models import User

from agenda.models.models import Agendamento
from agenda.serializers.serializers import AgendamentoSerializer, CriarEnderecoParaPrestadorSerializer, PrestadorSerializer, EndereçoSerializer
from agenda.tasks import gera_relatorio_prestadores_csv
from agenda.utils import get_horarios_disponiveis


class IsOwnerDrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        username = request.query_params.get('username', None)
        if request.user.username == username:
            return True
        return False
    
    
class IsPrestador(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.prestador == request.user:
            return True
        return False


class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView): # /api/agendamentos/<pk>/
    serializer_class = AgendamentoSerializer
    permission_classes = [IsOwnerDrCreateOnly]
    
    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Agendamento.objects.filter(prestador__username=username)
    
    
class AgendamentoList(generics.ListCreateAPIView): # /api/agendamentos/<pk>/
    permission_classes = [IsPrestador]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
    

    
@api_view(http_method_names=['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_relatorio_prestadores(request):
    
    if request.query_params.get('formato') == "csv":
        result = gera_relatorio_prestadores_csv.delay()
        return Response({"task_id": result.task_id})
    else:
        prestadores = User.objects.all()
        serializer = PrestadorSerializer(prestadores, many=True)
        return Response(serializer.data)
    
    
@api_view(['POST'])
def prestador_endereco(request, pk):
    prestador = get_object_or_404(User, pk=pk)
    serializer = CriarEnderecoParaPrestadorSerializer(data=request.data, context={'prestador': prestador})
    if serializer.is_valid():
        endereco = serializer.save()
        return Response(EndereçoSerializer(endereco).data, status=201)
    return Response(serializer.errors, status=400)
        
        
@api_view(http_method_names=['GET'])
def get_horarios(request):
    data = request.query_params.get('data')
    if not data:
        data = datetime.now().date()
    try:
        data = datetime.fromisoformat(data).date()
    except ValueError:
        return JsonResponse({"error": "Data inválida. Use o formato YYYY-MM-DD."}, status=400)
        
        
    horarios_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return JsonResponse(horarios_disponiveis, safe=False)


class PrestadorList(generics.ListAPIView):
    """
    Lista os prestadores (User) com o serializer PrestadorSerializer.
    """
    queryset = User.objects.all()
    serializer_class = PrestadorSerializer
    permission_classes = [permissions.AllowAny]