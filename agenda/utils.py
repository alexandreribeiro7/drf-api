from datetime import date, time, datetime, timedelta, timezone
from typing import Iterable

import requests
from agenda.libs import brasil_api
from agenda.models.models import Agendamento

def get_horarios_disponiveis(data: date) -> Iterable[datetime]:
    """
    Retorna os horários disponíveis para agendamento em um determinado dia.
    Considera horários das 08:00 às 18:00, de hora em hora, e exclui os já agendados.
    """
    if brasil_api.is_feriado(data):
        return []
    
    start = datetime(year=data.year, month=data.month, day=data.day, hour=8, minute=0, tzinfo=timezone.utc)
    end = datetime(year=data.year, month=data.month, day=data.day, hour=18, minute=0, tzinfo=timezone.utc)
    delta = timedelta(hours=1)
    horarios_disponiveis = []
    agendados = set(
        (dt.hour, dt.minute)
        for dt in Agendamento.objects.filter(data_horario__date=data)
        .values_list('data_horario', flat=True)
    )
    current = start
    while current < end:
        if (current.hour, current.minute) not in agendados:
            horarios_disponiveis.append(current)
        current += delta  # incrementa current!
    return horarios_disponiveis