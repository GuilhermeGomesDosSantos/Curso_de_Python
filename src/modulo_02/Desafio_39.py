# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou sejá passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Ano de Nascimento: "))

if (anoAtual - anoNascimento) <= 17:
    print(
        "Ainda faltam {} ano(s) para o alistamento".format(
            18 - (anoAtual - anoNascimento)
        )
    )
    print(
        "Seu alistamento será em {}".format(
            (18 - (anoAtual - anoNascimento)) + anoAtual
        )
    )
elif (anoAtual - anoNascimento) > 18:
    print(
        "Você já deveria ter se alistado há {} ano(s)".format(
            (anoAtual - anoNascimento) - 18
        )
    )
else:
    print("Você tem que se alistar IMEDIATAMENTE!")
