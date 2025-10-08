from datetime import date, datetime
import logging
from django.conf import settings

import requests


def is_feriado(data: date) -> bool:
    logging.info(f"Verificando se {data} é feriado")
    if settings.TESTING == True:
        logging.info("requisição não está sendo feita porque está em modo de teste")
        if date.day == 25 and date.month == 12:
            return True
        return False
    
    ano = data.year
    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if r.status_code != 200:
        logging.error(f"Erro ao consultar feriados: {r.status_code} - {r.text}")
        return False  # Se não conseguir consultar, assume que não é feriado
    feriados = r.json()
    for feriado in feriados:
        data_feriado_as_str = feriado["date"]
        data_feriado = datetime.fromisoformat(data_feriado_as_str).date()
        if data == data_feriado:
            return True
    return False
