from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

from agenda.models.models import Agendamento
from agenda.serializers.serializers import AgendamentoSerializer


class AgendamentoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    
    def get(self, request, id, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def patch(self, request, id, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def put(self, request, id, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, id, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class AgendamentoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)