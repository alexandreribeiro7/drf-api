import csv


with open ("exemplo_2.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow (["nome", "email", "telefone"])
    writer.writerow (["João", "joao@gmail.com", "11999999999"])
    writer.writerow (["Maria", "maria@gmail.com", "11888888888"])
    writer.writerow (["Pedro", "pedro@gmail.com", "11777777777"])