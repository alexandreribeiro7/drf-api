# API


- Listar horarios: GET /horarios/
- ["07:00, "19:30"]


- Listar agendamentos: GET /agendamentos/
[
    {
        "nome", "Nombre",
        "telefone", "123414344"
        "email", "exemplo@gmail.com
}
]

- ### Configuração .env 
- DJANGO_SETTINGS_MODULE=tamarcado.settings
- PYTHONPATH=. 

-------------------------------

- ### EndPoints
- Detalhar agendamento: GET /agendamentos/<id>/

- Criar agendamento: POST /agendamentos/

- Excluir agendamento: DELETE /agendamentos/<id>/

- Editar um agendamento: PUT/PATCH/agendamentos/<id>/