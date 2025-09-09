from datetime import date, datetime
from django.conf import settings

import requests


def is_feriado(data: date) -> bool:
    if settings.TESTING == True:
        if date.day == 25 and date.month == 12:
            return True
        return False
    
    ano = data.year
    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if r.status_code != 200:
        return False  # Se não conseguir consultar, assume que não é feriado
    feriados = r.json()
    for feriado in feriados:
        data_feriado_as_str = feriado["date"]
        data_feriado = datetime.fromisoformat(data_feriado_as_str).date()
        if data == data_feriado:
            return True
    return False
