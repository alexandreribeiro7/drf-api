# API


Listar horarios: GET /horarios/
["7:00", "19:30"]

Listar agendamentos: GET /agendamentos/
[
    {
        "nome": "Fulano",
        "telefone": "1234567",
        "email": "fulano@gmail.com"
    }
]


Detalhar agendamento: GET /agendamentos/<id>/
...

Criar agendamento: POST /agendamentos/

Excluir agendamento: DELETE /agendamento/<id>/

Editar agendamento: PUT/PATH /agendamento/<id>/