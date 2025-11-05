import csv
from io import StringIO
import csv

from django.core.mail import EmailMessage

from agenda.serializers.serializers import PrestadorSerializer
from django.contrib.auth.models import User
from tamarcado.celery import app
from django.conf import settings

@app.task
def gera_relatorio_prestadores_csv():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow([
        'id',
        'username',
        'data_horario',
        'nome_cliente',
        'telefone_cliente',
        'email_cliente',
    ])
    
    prestadores = User.objects.all()
    serializer = PrestadorSerializer(prestadores, many=True)
    for prestador in serializer.data:
        for ag in prestador.get('agendamentos', []):
            writer.writerow([
                prestador.get('id'),
                prestador.get('username'),
                ag.get('data_horario'),
                ag.get('nome_cliente'),
                ag.get('telefone_cliente'),
                ag.get('email_cliente'),
            ])
    
    email = EmailMessage(
        'tamarcado - Relatório de Prestadores',
        'Segue em anexo o relatório de prestadores em formato CSV.',
        'teste23@gmail.com',
        ['teste2345@gmail.com'],
    )

    email.attach('relatorio_prestadores.csv', output.getvalue(), "text/csv")
    email.send()