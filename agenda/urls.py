from django.urls import path

from agenda.views.views import AgendamentoDetail, AgendamentoList

urlpatterns = [
    path("agendamentos/", AgendamentoList.as_view(), name="agendamento-list"),
    path("agendamentos/<int:pk>/", AgendamentoDetail.as_view(), name="agendamento-detail")
]