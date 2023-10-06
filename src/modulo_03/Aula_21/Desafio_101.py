# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO


def voto(anoNascimento):
    import datetime

    anoAtual = datetime.date.today().year
    idade = anoAtual - anoNascimento

    if idade >= 16 and idade <= 18 or idade >= 65:
        return f"A sua Idade é: {idade}, então o voto é OPCIONAL"
    elif idade < 16:
        return f"A sua Idade é: {idade}, então o voto é NEGADO"
    else:
        return f"A sua Idade é {idade}, então o voto é OBRIGATÓRIO"


anoNascimento = int(input("Em que ano você Nasceu? "))
print(voto(anoNascimento))
