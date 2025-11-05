from django.urls import path

from agenda.views.views import AgendamentoDetail, AgendamentoList, PrestadorList, get_horarios, get_relatorio_prestadores, prestador_endereco

urlpatterns = [
    path("agendamentos/", AgendamentoList.as_view(), name="agendamento-list"),
    path("agendamentos/<int:pk>/", AgendamentoDetail.as_view(), name="agendamento-detail"),
    path("prestadores/", get_relatorio_prestadores),
    path("prestadores/<int:pk>/enderecos/", prestador_endereco, name="prestador-endereco"),
    path("horarios/", get_horarios, name="horarios"),
]