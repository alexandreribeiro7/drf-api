import datetime
import json
from datetime import datetime, timezone
from django.test import TestCase
from rest_framework.test import APIClient

from agenda.models.models import Agendamento

# Teste de listagem de agendamentos utilizando Django TestCase e APIClient do Django REST Framework.
# Pode ser executado tanto com o runner padrão do Django quanto com o PyTest.

class TestListagemAgendamentos(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_listagem_vazia(self):
        response = self.client.get('/api/agendamentos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])
        
    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(
            data_horario=datetime(2022, 3, 15, tzinfo=timezone.utc),
            nome_cliente='Cliente 1',
            email_cliente='teste@gmail.com',
            telefone_cliente='123456789',
        )
class TestCriacaoAgendamento(TestCase):
            def setUp(self):
                self.client = APIClient()

            def test_criar_agendamento(self):
                agendamento_request_data = {
                    'data_horario': '2025-12-15T00:00:00Z',
                    'nome_cliente': 'Cliente 1',
                    'email_cliente': 'teste@gmail.com',
                    'telefone_cliente': '123456789',
                }
                response = self.client.post('/api/agendamentos/', agendamento_request_data, format='json')
                self.assertEqual(response.status_code, 201)
                agendamento_criado = Agendamento.objects.first()
                self.assertIsNotNone(agendamento_criado)
                self.assertEqual(
                    agendamento_criado.data_horario.isoformat().replace('+00:00', 'Z'),
                    agendamento_request_data['data_horario']
                )
                self.assertEqual(agendamento_criado.nome_cliente, agendamento_request_data['nome_cliente'])
                self.assertEqual(agendamento_criado.email_cliente, agendamento_request_data['email_cliente'])
                self.assertEqual(agendamento_criado.telefone_cliente, agendamento_request_data['telefone_cliente'])

            def test_quando_request_invalido_retorna_400(self):
                agendamento_request_data = {
                    'data_horario': '2023-10-01T10:00:00Z',
                    'nome_cliente': 'Cliente 1',
                    'telefone_cliente': '123456789',
                }
                response = self.client.post('/api/agendamentos/', agendamento_request_data, format='json')
                self.assertEqual(response.status_code, 400)

            def test_criar_agendamento_com_data_invalida(self):
                agendamento_request_data = {
                    'data_horario': 'invalid-date',
                    'nome_cliente': 'Cliente 1',
                    'email_cliente': 'teste@gmail.com',
                    'telefone_cliente': '123456789',
                }
                response = self.client.post('/api/agendamentos/', agendamento_request_data, format='json')
                self.assertEqual(response.status_code, 400)

            def test_nao_cria_agendamento_duplicado(self):
                agendamento_request_data = {
                    'data_horario': '2023-10-01T10:00:00Z',
                    'nome_cliente': 'Cliente 1',
                    'email_cliente': 'teste@gmail.com',
                    'telefone_cliente': '123456789',
                }
                self.client.post('/api/agendamentos/', agendamento_request_data, format='json')
                response = self.client.post('/api/agendamentos/', agendamento_request_data, format='json')
                # Supondo que duplicados não são permitidos
                self.assertIn(response.status_code, [400, 409])