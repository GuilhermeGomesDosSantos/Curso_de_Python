# A Confederação nacional de natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 25 anos: SÊNIOR
# -Acima: MASTER

from datetime import date

anoAtual = date.today().year

anoNascimento = int(input('Ano de Nascimento: '))
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Idade: {} anos, MIRIM'.format(idade))
elif idade <= 14:
    print('Idade: {}, INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade: {}, JUNIOR'.format(idade))
elif idade <= 25:
    print('Idade: {}, SÊNIOR'.format(idade))
else:
    print('Idade: {}, MASTER'.format(idade))